from route import check, db, api, get, up
from flask import Flask, session, request, render_template, flash
from flask_bcrypt import Bcrypt
import datetime
import os
import threading

app = Flask(__name__)
bcrypt = Bcrypt()
app.config["SECRET_KEY"] = os.urandom(21)
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=60)

HTML_PATH_HOME = './home.html'
HTML_PATH_INDEX = './index.html'
HTML_PATH_REGISTER = './signup.html'
HTML_PATH_APISET = './api_setting.html'
HTML_PATH_ITEMLIST = './item_list.html'
HTML_PATH_SCRAPSTART = './item_scraping_start.html'
HTML_PATH_SCRAP = './item_scraping.html'
HTML_PATH_MYPAGE = './mypage.html'

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
        data = db.db_connector(f'''SELECT ssid, sspw, atid, atpw, cpid, cpcode, cpak, cpsk, cpday, elevenapi, rtapi, rtday, wpid, wppw FROM apikey WHERE userid="{userid}"";''')

        ssid = data.split(' ')[0]
        sspw = data.split(' ')[1]
        atid = data.split(' ')[2]
        atpw = data.split(' ')[3]
        cpid = data.split(' ')[4]
        cpcode = data.split(' ')[5]
        cpak = data.split(' ')[6]
        cpsk = data.split(' ')[7]
        cpday = data.split(' ')[8]
        elevenapi = data.split(' ')[9]
        rtapi = data.split(' ')[10]
        rtday = data.split(' ')[11]
        wpid = data.split(' ')[12]
        wppw = data.split(' ')[13]
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

        db.db_connector(f"INSERT INTO apikey(ssid, sspw, atid, atpw, cpid, cpcode, cpak, cpsk, cpday, elevenapi, rtapi, rtday, wpid, wppw) VALUES('{ssid}', '{sspw}', '{atid}', '{atpw}', '{cpid}', '{cpcode}', '{cpak}', '{cpsk}', '{cpday}', '{elevenapi}', '{rtapi}', '{rtday}', '{wpid}', '{wppw}');")
        flash('적용되었습니다.')
        return render_template(HTML_PATH_APISET, username=session['user'], userplan=session['userplan'], ssid=ssid, sspw=sspw, atid=atid, atpw=atpw, cpid=cpid, cpcode=cpcode, cpak=cpak, cpsk=cpsk, cpday=cpday, elevenapi=elevenapi, rtapi=rtapi, rtday=rtday, wpid=wpid, wppw=wppw)

@app.route('/itemlist', methods=['GET', 'POST'])
def itemlist():
    if not check.login:
        return render_template(HTML_PATH_INDEX)

    if request.method == 'GET':
        try:
            productid = db.db_connector(f'''SELECT productid FROM userproduct WHERE userid="{session['user']}";''')
            title = db.db_connector(f'''SELECT title FROM taobao WHERE userid="{productid}";''')
            propprice = db.db_connector(f'''SELECT price FROM prop WHERE userid="{productid}";''')
            taobaoimg = db.db_connector(f'''SELECT img FROM taobaoimg WHERE userid="{productid}";''')
            propimg = db.db_connector(f'''SELECT img FROM prop WHERE userid="{productid}";''')
        except:
            return render_template(HTML_PATH_ITEMLIST, username=session['user'], userplan=session['userplan'], isitem=False)

        print(title)
        print(type(title))
        print(propprice)
        print(type(propprice))
        return render_template(HTML_PATH_ITEMLIST, username=session['user'], userplan=session['userplan'], isitem=True, productid=productid, title=title, propprice=propprice, taobaoimg=taobaoimg, propimg=propimg)

    if request.method == 'POST':
        productid = db.db_connector(f'''SELECT productid FROM userproduct WHERE userid="{session['user']}";''')
        title = db.db_connector(f'''SELECT title FROM taobao WHERE userid="{productid}";''')
        propprice = db.db_connector(f'''SELECT price FROM prop WHERE userid="{productid}";''')
        taobaoimg = db.db_connector(f'''SELECT img FROM taobaoimg WHERE userid="{productid}";''')
        propimg = db.db_connector(f'''SELECT img FROM prop WHERE userid="{productid}";''')
        # 데이터 스플릿 해서 셀레니움에 집어넣기
        threading.Thread(target=up.upload, args=(1,1,title,propprice,1000,"test")).start()
        flash("업로드 완료되었습니다.")
        # 셀레니움 작동 시키기

@app.route('/itemscrap', methods=['GET', 'POST'])
def itemscrap():
    if not check.login:
        return render_template(HTML_PATH_INDEX)

    if request.method == 'GET':
        return render_template(HTML_PATH_SCRAP, username=session['user'], userplan=session['userplan'])
    elif request.method == 'POST':
        try:
            taobao = request.form.get('scrap')
            print(taobao)
            print(type(taobao))
            result = api.taobao(taobao)

            product_id = str(result['item']['num_iid']) # 상품번호
            title = result['item']['title'] # 상품제목
            price = result['item']['price'] # 상품 가격(할인 적용)
            orginal_price = result['item']['orginal_price'] # 상품 가격 (할인 미적용)
            product_imgurl = result['item']['item_imgs']#[0]['url'] # 상품 사진 링크
            desc_imgurl = result['item']['desc_img'] # 상품 설명 사진, 없을 수 도 있음.
            prop_price = result['item']['skus']['sku']#[0]['price'] # 옵션 가격 (할인 적용)
            prop_orginalprice = result['item']['skus']['sku']#[0]['orginal_price'] # 옵션 가격 (할인 미적용)
            prop_imgurl = result['item']['prop_imgs']['prop_img']#[0]['url'] # 옵션 사진 링크
            propname = result['item']['skus']['sku']#[0]['properties_name'] # 옵션 이름
            propid = str(result['item']['skus']['sku'])#[0]['sku_id']) # 옵션 id

            for i, n in enumerate(product_imgurl):
                get.imgpt(n['url'], product_id, i) # 사진을 폴더에 저장
                product_img = product_id + "_" + i
                product_img = "../static/taobao_img/"+product_img+".png"
                db.db_connector(f"INSERT INTO taobaoimg(productid, img) VALUES('{product_id}', '{product_img}');")

            if desc_imgurl:
                for i, n in enumerate(desc_imgurl):
                    get.imgpt(n, product_id, i) # 사진을 폴더에 저장
                    desc_img = product_id + "_" + i
                    desc_img = "../static/desc_img/"+desc_img+".png"
                    db.db_connector(f"INSERT INTO descimg(productid, img) VALUES('{product_id}', '{desc_img}');")
            
            for i, n in enumerate(prop_imgurl):
                get.imgpp(n['url'], propid, i) # 사진을 폴더에 저장

            prop_img = "../static/prop_img/"+propid+".png" # 상대경로를 DB에 저장

            db.db_connector(f"INSERT INTO taobao(productid, title, price, orginalprice) VALUES('{product_id}', '{title}', '{price}', '{orginal_price}');")
            db.db_connector(f"INSERT INTO prop(propid, productid, propname, price, orginalprice, img) VALUES('{propid}', {product_id}', '{propname}', '{prop_price}', '{prop_orginalprice}' '{prop_img}');")
            db.db_connector(f"INSERT INTO userproduct(userid, productid) VALUES('{session['user']}', '{product_id}');")

            return render_template(HTML_PATH_SCRAP, username=session['user'], userplan=session['userplan'], result=True, successcount=1, count=1)
        except:
            return render_template(HTML_PATH_SCRAP, username=session['user'], userplan=session['userplan'], result=True, failcount=1, count=1)

if __name__ == '__main__':
    app.run(host="localhost", port="5555", debug=True, threaded=True)