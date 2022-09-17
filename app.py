from route import check, db, api, get, up
from flask import Flask, session, request, render_template, flash, redirect, url_for
from flask_bcrypt import Bcrypt
from urllib.parse import urlparse, parse_qs
import datetime
import os
import threading

app = Flask(__name__)
bcrypt = Bcrypt()
#app.config["SECRET_KEY"] = os.urandom(55)
app.config["SECRET_KEY"] = f"dsfiji38jhjsdfjojidsfh832hdsifjiopasdkmmvcdikjuhed9w329hd"
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=60)

HTML_PATH_HOME = './home.html'
HTML_PATH_INDEX = './index.html'
HTML_PATH_REGISTER = './signup.html'
HTML_PATH_APISET = './api_setting.html'
HTML_PATH_ITEMLIST = './item_list.html'
HTML_PATH_SCRAPSTART = './item_scraping_start.html'
HTML_PATH_SCRAP = './item_scraping.html'
HTML_PATH_MYPAGE = './mypage.html'

def gettotalpage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if check.login():
            return render_template(HTML_PATH_HOME, username=session['user'], userplan=session['userplan'])
        return render_template(HTML_PATH_INDEX)

    elif request.method == 'POST':
        userid = request.form.get('username')
        userpw = request.form.get('password')

        if not (userid and userpw):
            flash("모두 입력해주세요")
            return render_template(HTML_PATH_INDEX, ErrorTitle="ERROR! ", ErrorMessage="모두 입력해주세요.")

        realuserpw = db.db_connector(f'''SELECT userpw FROM usertbl WHERE userid="{userid}";''')

        if bcrypt.check_password_hash(realuserpw, userpw):
            userplan = db.db_connector(f'''SELECT userplan FROM usertbl WHERE userid="{userid}";''')
            session['user'] = userid
            session['userplan'] = userplan
            return render_template(HTML_PATH_HOME, username=session['user'], userplan=session['userplan'])
        else:
            return render_template(HTML_PATH_INDEX, ErrorTitle="ERROR! ", ErrorMessage="Username/Password does not exist")
       
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if check.login():
            return render_template(HTML_PATH_HOME, username=session['user'], userplan=session['userplan'])
        return render_template(HTML_PATH_REGISTER)

    elif request.method == 'POST':
        if 'file' not in request.files:
            flash('사업자등록증을 첨부해주세요.')

        userid = request.form.get('username')
        userpw = request.form.get('password')
        reuserpw = request.form.get('repassword')
        username = request.form.get('name')
        phone_number = request.form.get('phone_number')
        business_number = request.form.get('business_number')
        business_pic = request.files['file']

        business_pic.save("./data/b_img/{}.png".format(userid))

        if not (userid and userid and userpw and reuserpw):
            flash("모두 입력해주세요.")
            return render_template(HTML_PATH_INDEX, ErrorTitle="ERROR! ", ErrorMessage="모두 입력해주세요.")
        if userpw != reuserpw:
            flash("비밀번호가 다릅니다.")
            return render_template(HTML_PATH_INDEX, ErrorTitle="ERROR! ", ErrorMessage="비밀번호가 다릅니다.")
        
        checkusername = db.db_connector(f'''SELECT userid FROM usertbl WHERE userid="{userid}";''')
        if checkusername == "":
            pw_hash = bcrypt.generate_password_hash(userpw).decode('utf-8')
            db.db_connector(f"INSERT INTO usertbl(userid, userpw, userplan, username, phone_number, business_number) VALUES('{userid}', '{pw_hash}', 'FREE', '{username}', '{phone_number}', '{business_number}');")
            flash("가입에 성공하였습니다.")
            return render_template(HTML_PATH_INDEX, ErrorTitle="NOTICE! ", ErrorMessage="Register Success")
        else:
            flash("이미 가입된 이메일입니다.")
            return render_template(HTML_PATH_REGISTER, ErrorTitle="ERROR! ", ErrorMessage="Username already exist")

@app.route('/home', methods=['GET'])
def home():
    if not check.login:
        return render_template(HTML_PATH_INDEX)
    return render_template(HTML_PATH_HOME, username=session['user'], userplan=session['userplan'])

@app.route('/mypage', methods=['GET'])
def mypage():
    if not check.login:
        return render_template(HTML_PATH_INDEX)
    return render_template(HTML_PATH_MYPAGE, username=session['user'], userplan=session['userplan'])

@app.route('/api_setting', methods=['GET', 'POST']) 
def apiset():
    if not check.login:
        return render_template(HTML_PATH_INDEX)

    if request.method =='GET':
        userid = session['user']
        try:
            data = db.db_connector(f'''SELECT ssid, sspw, atid, atpw, cpid, cpcode, cpak, cpsk, cpday, elevenapi, rtapi, rtday, wpid, wppw FROM apikey WHERE userid="{userid}"";''').split()
        except:
            return render_template(HTML_PATH_APISET, username=session['user'], userplan=session['userplan'])

        ssid = data[0]; sspw = data[1]
        atid = data[2]; atpw = data[3]
        cpid = data[4]; cpcode = data[5]; cpak = data[6]; cpsk = data[7]; cpday = data[8]
        elevenapi = data[9]
        rtapi = data[10]; rtday = data[11]
        wpid = data[12]; wppw = data[13]
        return render_template(HTML_PATH_APISET, username=session['user'], userplan=session['userplan'], ssid=ssid, sspw=sspw, atid=atid, atpw=atpw, cpid=cpid, cpcode=cpcode, cpak=cpak, cpsk=cpsk, cpday=cpday, elevenapi=elevenapi, rtapi=rtapi, rtday=rtday, wpid=wpid, wppw=wppw)

    elif request.method =='POST':
        ssid = request.form.get('ssid')
        sspw = request.form.get('sspw')
        atid = request.form.get('atid')
        atpw = request.form.get('atpw')
        cpid = request.form.get('cpid')
        cpcode = request.form.get('cpcode')
        cpak = request.form.get('cpak')
        cpsk = request.form.get('cpsk')
        cpday = request.form.get('cpday')
        elevenapi = request.form.get('elevenapi')
        rtapi = request.form.get('rtapi')
        rtday = request.form.get('rtday')
        wpid = request.form.get('wpid')
        wppw = request.form.get('wppw')

        db.db_connector(f"REPLACE INTO apikey(userid, ssid, sspw, atid, atpw, cpid, cpcode, cpak, cpsk, cpday, elevenapi, rtapi, rtday, wpid, wppw) VALUES('{session['user']}', '{ssid}', '{sspw}', '{atid}', '{atpw}', '{cpid}', '{cpcode}', '{cpak}', '{cpsk}', '{cpday}', '{elevenapi}', '{rtapi}', '{rtday}', '{wpid}', '{wppw}');")
        flash('적용되었습니다.')
        return render_template(HTML_PATH_APISET, username=session['user'], userplan=session['userplan'], ssid=ssid, sspw=sspw, atid=atid, atpw=atpw, cpid=cpid, cpcode=cpcode, cpak=cpak, cpsk=cpsk, cpday=cpday, elevenapi=elevenapi, rtapi=rtapi, rtday=rtday, wpid=wpid, wppw=wppw)

@app.route('/itemlist/<int:listid>', methods=['GET'])
def itemlist(listid):
    if not check.login:
        return render_template(HTML_PATH_INDEX)

    try:
        productid = db.db_connector(f'''SELECT productid FROM userproduct WHERE userid="{session['user']}";''').split()
        title = []
        prop = []
        taoimg = []
        descimg = []
        for i in productid:
            title.append(db.db_connector(f'''SELECT title FROM taobao WHERE productid="{i}";'''))
            prop.append(db.db_connector(f'''SELECT propid, propname, price, img FROM prop WHERE productid="{i}";''').split())
            taoimg.append(db.db_connector(f'''SELECT img FROM taobaoimg WHERE productid="{i}";''').split())
            descimg.append(db.db_connector(f'''SELECT img FROM descimg WHERE productid="{i}";''').split())
        
    except:
        return render_template(HTML_PATH_ITEMLIST, username=session['user'], userplan=session['userplan'], isitem=False)

    pagecount = gettotalpage(len(productid), 20)

    # 없는 페이지를 접속 시 아이템을 반환하지 않음.
    if pagecount < listid:
        return render_template(HTML_PATH_ITEMLIST, username=session['user'], userplan=session['userplan'], isitem=False)

    if not listid == 1:
        startpage = listid * 20
        endpage = listid * 21
    else:
        startpage = 0
        endpage = 20

    productid2 = []
    title2 = []
    prop2 = []
    taoimg2 = []
    descimg2 = []
    
    #for i in range(startpage, endpage):
     #   productid2.append(productid[i])
      #  title2.append(title[i])
       # prop2.append(prop[i])
        #taoimg2.append(taoimg[i])
        #descimg2.append(descimg[i])
    
    return render_template(HTML_PATH_ITEMLIST, username=session['user'], userplan=session['userplan'], isitem=True, productid=productid, title=title, prop=prop, taoimg=taoimg, descimg=descimg, listid=listid, endpage=endpage, startpage=startpage)

@app.route('/itemlist', methods=['POST'])
def itemlistup():
    if not check.login:
        return render_template(HTML_PATH_INDEX)

    productids = request.form.get('pid')
    title = db.db_connector(f'''SELECT title FROM taobao WHERE productid="{productids}";''')
    propname = db.db_connector(f'''SELECT propname FROM prop WHERE productid="{productids}";''').split()
    propprice = db.db_connector(f'''SELECT price FROM prop WHERE productid="{productids}";''').split()
    proppic = db.db_connector(f'''SELECT img FROM prop WHERE productid="{productids}";''').split()
    propid = db.db_connector(f'''SELECT propid FROM prop WHERE productid="{productids}";''').split()

    prop = []
    for n, i in enumerate(propname):
        # 문자열 리스트화
        a = []
        a.append(i)

        # 옵션(리스트)에 옵션 이름(리스트) 넣기 - 2차원
        prop.append(a)

    for n, i in enumerate(prop):
        prop[n].append(propprice[n])
        prop[n].append(proppic[n])
        prop[n].append(propid[n])
        
    threading.Thread(target=up.ssupload, args=(1,1,title,1000000,10000,"by dino", prop)).start()
    flash("업로드 완료되었습니다.")

    return redirect(url_for('itemlist', listid=1))

@app.route('/itemscrap', methods=['GET', 'POST'])
def itemscrap():
    if not check.login:
        return render_template(HTML_PATH_INDEX)

    if request.method == 'GET':
        return render_template(HTML_PATH_SCRAP, username=session['user'], userplan=session['userplan'])
    elif request.method == 'POST':
        try:
            taobao = request.form.get('scrap')
            params = parse_qs(urlparse(taobao).query)
            id = params['id']
            success_count = 0
            fail_count = 0
            for id in id:
                try:
                    result = api.taobao(id)

                    product_id = str(result['item']['num_iid']) # 상품번호
                    title = result['item']['title'] # 상품제목
                    price = result['item']['price'] # 상품 가격(할인 적용)
                    orginal_price = result['item']['orginal_price'] # 상품 가격 (할인 미적용)
                    product_imgurl = result['item']['item_imgs'] # 상품 사진 링크
                    desc_imgurl = result['item']['desc_img'] # 상품 설명 사진, 없을 수 도 있음.
                    prop = result['item']['skus']['sku'] # 옵션
                    prop_imgurl = result['item']['prop_imgs']['prop_img'] # 옵션 사진
                    
                    for i, n in enumerate(product_imgurl):
                        get.imgpt(n['url'], product_id, i) # 사진을 폴더에 저장
                        product_img = "{}_{}".format(product_id, i)
                        product_img = "../static/taobao_img/"+product_img+".png"
                        db.db_connector(f"INSERT INTO taobaoimg(productid, img) VALUES('{product_id}', '{product_img}');")

                    if len(desc_imgurl) > 0:
                        for i, n in enumerate(desc_imgurl):
                            get.imgdc(n, product_id, i) # 사진을 폴더에 저장
                            desc_img = "{}_{}".format(product_id, i)
                            desc_img = "../static/desc_img/"+desc_img+".png"
                            db.db_connector(f"INSERT INTO descimg(productid, img) VALUES('{product_id}', '{desc_img}');")
                    
                    for i, n in enumerate(prop):
                        get.imgpp(prop_imgurl[i]['url'], n['properties']) # 사진을 폴더에 저장
                        prop_img = "../static/prop_img/"+n['properties']+".png"
                        prop_name = n['properties_name'].split(':')[3]
                        db.db_connector(f"REPLACE INTO prop(propid, productid, propname, price, orginalprice, img) VALUES('{n['properties']}', '{product_id}', '{prop_name}', '{n['price']}', '{n['orginal_price']}', '{prop_img}');")
                    
                    db.db_connector(f"REPLACE INTO taobao(productid, title, price, orginalprice) VALUES('{product_id}', '{title}', '{price}', '{orginal_price}');")

                    # 중복 검사 구문
                    try:
                        productid = db.db_connector(f'''SELECT productid FROM userproduct WHERE userid="{session['user']}";''').split()
                        if not "{}".format(product_id) in productid:
                            db.db_connector(f"INSERT INTO userproduct(userid, productid) VALUES('{session['user']}', '{product_id}');")
                    except:
                        db.db_connector(f"INSERT INTO userproduct(userid, productid) VALUES('{session['user']}', '{product_id}');")

                    success_count += 1
                except:
                    fail_count += 1

            flash('수집 완료')
            return render_template(HTML_PATH_SCRAP, username=session['user'], userplan=session['userplan'], isresult=True, successcount=success_count, failcount=fail_count, count=success_count+fail_count)
        except:
            flash("수집 실패")
            return render_template(HTML_PATH_SCRAP, username=session['user'], userplan=session['userplan'], isresult=True, failcount="오류", successcount="오류", count="오류")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5555", threaded=True)