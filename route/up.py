from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from route.wcaptcha import captcha_predict
import time
import random
import os
import requests

def ssupload(nid, pw, taotitle, taoprice, taoqa, taocontent, prop):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://sell.smartstore.naver.com/#/home/about")
    wait = WebDriverWait(driver, 10)

    login_form = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[2]/div[2]/div/div[1]/div[2]/button[1]/span")))
    login_form.click()

    username = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/div/div[4]/div[1]/div/ul[1]/li[1]/input")))
    password = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/div/div[4]/div[1]/div/ul[1]/li[2]/input")))

    username.send_keys(nid)
    time.sleep(2)
    password.send_keys(pw)
    time.sleep(1)

    login = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/div/div[4]/div[1]/div/div/button")))
    login.click()

    time.sleep(3)

    driver.get("https://sell.smartstore.naver.com/#/products/create")


    time.sleep(0.3)

    cate = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[2]/div/div/div[1]/input")))
    cate.send_keys("패")
    time.sleep(1)
    cate.send_keys(Keys.ENTER)

    time.sleep(1)

    title = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[7]/div/div[2]/div/div/div/div/div/div/input")))
    title.send_keys(taotitle)

    time.sleep(0.3)

    price = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"prd_price2\"]")))
    price.send_keys(taoprice)

    time.sleep(0.3)

    qa = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"stock\"]")))
    qa.send_keys(taoqa)

    time.sleep(0.3)

    driver.execute_script("window.scrollTo(0, 2200)") 

    time.sleep(1)

    change = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[13]/div/div[2]/div/div/ncp-editor-form/div[1]/ul/li[2]/a")))
    change.click()

    content = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[13]/div/div[2]/div/div/ncp-editor-form/div[1]/div/div/textarea")))
    content.send_keys(taocontent)

    driver.execute_script("window.scrollTo(0, 1300)") 

    time.sleep(1)

    uploadimg = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[12]/div/div[2]/div/div[1]/div/div/ncp-photo-infra-image-upload/div/div[1]/div/ul/li/div/a")))
    uploadimg.click()

    time.sleep(1)

    #taoimg1 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/button[1]")))
    #taoimg1.click()

    taoimg = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    taoimg.send_keys(r"/home/hj/문서/GitHub/dino/a.png")

    time.sleep(2)

    # 여기부터 옵션

    options = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/div/div/div/a")))
    options.click()

    time.sleep(1)

    options =  wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/fieldset/div/div/div[1]/div/div/div/div/label[1]")))
    options.click()

    time.sleep(0.3)

    try:
        options =  wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[1]/div/div[2]/label[1]")))
        options.click()
    except:
        pass

    driver.execute_script("window.scrollTo(0, 1550)") 

    time.sleep(1)

    options = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"choice_option_name0\"]")))
    options.send_keys("옵션")

    options = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"choice_option_value0\"]")))
    options.send_keys("옵션")

    options = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div[4]/div/div/div[2]/div[1]/a")))
    options.click()

    for n, i in enumerate(prop):
        if not n == 0:
            options = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/a")))
            options.click()
            time.sleep(0.5)

        oname = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[{}]/div[2]".format(n+1))))
        oname.click()
        oname = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[{}]/div[2]/div/input".format(n+1))))
        oname.send_keys(i[0])

        time.sleep(0.5)

        oprice = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[{}]/div[3]".format(n+1))))
        oprice.click()
        oprice = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[{}]/div[3]/span/input".format(n+1))))
        oprice.send_keys(0)

        time.sleep(0.5)

        ocount = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[{}]/div[4]".format(n+1))))
        ocount.click()
        ocount = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[{}]/div[4]/span/input".format(n+1))))
        ocount.send_keys(1000)

        time.sleep(0.5)

        driver.execute_script("window.scrollTo(0, 1700)") 


    upload = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[3]/div[2]/div[1]/button[3]")))
    upload.click()

    try:
        uploaddone = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/button[1]")))
        uploaddone.click()
    except:
        pass

    time.sleep(30)

    driver.close()

def wpupload(wid, pw, taotitle, taoprice, taoqa, taocontent):
    options = FirefoxOptions()
    #options.add_argument('-headless')

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get("https://wpartner.wemakeprice.com/login")
    wait = WebDriverWait(driver, 5)

    rd = str(random.randrange(1,100000))
    rd = rd.replace('1', '2')
    rd = rd.replace('9', '8')
    rd = rd.replace('0', '3')

    time.sleep(2)

    try:
        while True:
            with open('./route/wcaptcha/dataset/predict/{}.png'.format(rd), 'wb') as file:
                file.write(driver.find_element(By.XPATH, '//*[@id="_captchaImage"]').screenshot_as_png)
            try:
                captcha = captcha_predict.main(rd)
                username = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[1]/div[1]/input[1]")))
                password = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[1]/div[1]/input[2]")))

                username.send_keys("junii0131")
                time.sleep(1)
                password.send_keys("45396861Wns!")
                time.sleep(1)

                capt = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"_captchaWord\"]")))
                capt.send_keys(captcha)
                time.sleep(1)

                login = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"login\"]")))
                login.click()

                isSuccess = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"login\"]")))

                os.system("rm ./wcaptcha/dataset/predict/{}.png".format(rd))

                if isSuccess:
                    break

            except:
                pass
    except:
        username = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[1]/div[1]/input[1]")))
        password = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[1]/div[1]/input[2]")))

        username.send_keys("junii0131")
        time.sleep(1)
        password.send_keys("45396861Wns!")
        time.sleep(1)

        login = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"login\"]")))
        login.click()

    time.sleep(2)

    driver.get("https://wpartner.wemakeprice.com/product/prodSet?setType=set")

    catego = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"cateSchNm\"]")))
    catego.send_keys("유아")

    category = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"cateSchNm\"]")))
    category.send_keys(Keys.RETURN)

    time.sleep(1)

    cate = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/form/div[4]/div[2]/div/table/tbody/tr[1]/td/div[2]/div/ul/li[1]")))
    cate.click()

    time.sleep(1)

    name = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"prodNm\"]")))
    name.send_keys("name")

    brand = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/form/div[4]/div[2]/div/table/tbody/tr[5]/td/div/div[2]/label/span")))
    brand.click()

    md = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/form/div[4]/div[2]/div/table/tbody/tr[7]/td/div/div[2]/label/span")))
    md.click()

    time.sleep(1)

    op = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"originPrice\"]")))
    op.send_keys("10000000")

    time.sleep(1)

    sp = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"salePrice\"]")))
    sp.send_keys("10000000")

    time.sleep(1)

    count = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"stockCount\"]")))
    count.send_keys("1000")

    time.sleep(1)

    taoimg = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"prodImgRegArea0\"]")))
    taoimg.click()

    time.sleep(1)

    taoimg = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/form/div[12]/div[2]/div/table/tbody/tr[3]/td/div[3]/div[1]/label/label/input")))
    taoimg.send_keys(r"/home/hj/문서/GitHub/dino/a.png") # 오류

    time.sleep(1)

    taoimg2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"prodImgRegArea3\"]")))
    taoimg2.click()

    time.sleep(1)

    taoimg2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/form/div[12]/div[2]/div/table/tbody/tr[3]/td/div[5]/div/label/label/input")))
    taoimg2.send_keys(r"/home/hj/문서/GitHub/dino/a.png") # 오류

    time.sleep(1)

    change = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/form/div[12]/div[2]/div/table/tbody/tr[4]/td/div[1]/label[2]/span")))
    change.click()

    time.sleep(1)

    iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)

    time.sleep(1)

    content = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body")))
    content.send_keys("1000")

    time.sleep(1)

    driver.switch_to.default_content()

    time.sleep(1)

    change = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"gnoticeNo_0\"]")))
    change.click()

    time.sleep(1)

    change = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/form/div[14]/div[2]/div/table/tbody/tr[2]/td/div/div[1]/select/option[2]")))
    change.click()

    time.sleep(1)

    change = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/form/div[14]/div[2]/div/table/tbody/tr[3]/td/div/div/div[1]/div/label/span")))
    change.click()

    time.sleep(1)

    up = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"setProdInfoBtn\"]")))
    up.click()

    time.sleep(1)

    driver.close()

def gaupload(wid, pw, taotitle, taoprice, taoqa, taocontent):
    options = ChromeOptions()
    #options.add_argument('-headless')

    driver = webdriver.Chrome("./chromedriver", options=options)
    driver.maximize_window()
    driver.get("https://www.esmplus.com/Member/SignIn/LogOn")
    wait = WebDriverWait(driver, 5)

    gm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/label[2]")))
    gm.click()

    username = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"SiteId\"]")))
    password = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"SitePassword\"]")))

    username.send_keys(wid)
    time.sleep(1)
    password.send_keys(pw)
    time.sleep(1)
 
    login = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/form/fieldset/div[2]/a/img")))
    login.click()

    time.sleep(1)

    mer = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/ul/li[1]/a")))
    mer.click()

    time.sleep(1)

    mer2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"TDM395\"]")))
    mer2.click()

    time.sleep(2)

    tabs = driver.window_handles

    i = 1
    while True:
        try:
            driver.switch_to.window(tabs[i])
            driver.close()
            i += 1
            time.sleep(1)
        except:
            break
    
    time.sleep(1)

    driver.switch_to.window(tabs[0])
    driver.switch_to.frame("ifm_TDM395")

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[1]/div/div[2]/select[1]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[1]/div/div[2]/select[1]/option[12]")))
    category.click()

    time.sleep(1)
    
    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[1]/div/div[2]/select[2]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[1]/div/div[2]/select[2]/option[2]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[1]/div/div[2]/select[3]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[1]/div/div[2]/select[3]/option[2]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div/div/div/div[2]/select[1]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div/div/div/div[2]/select[1]/option[2]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div/div/div/div[2]/select[2]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div/div/div/div[2]/select[2]/option[2]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div/div/div/div[2]/select[3]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div/div/div/div[2]/select[3]/option[2]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[3]/div/div/div/div[2]/select[1]")))
    category.click()
    
    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[3]/div/div/div/div[2]/select[1]/option[2]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[3]/div/div/div/div[2]/select[2]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[3]/div/div/div/div[2]/select[2]/option[2]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[3]/div/div/div/div[2]/select[3]")))
    category.click()

    time.sleep(1)

    category = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/table/tbody/tr[4]/td/div/div/div/div[3]/div/div/div/div[2]/select[3]/option[2]")))
    category.click()

    time.sleep(1)

    name = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"txtGoodsNameSearch\"]")))
    price = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"txtGoodsPrice\"]")))

    name.send_keys("1111111")
    time.sleep(1)
    price.send_keys("10000000")
    time.sleep(1)

    next = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/ol/li[2]/a")))
    next.click()

    time.sleep(1)

    taoimg = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/table/tbody/tr[1]/td/div/div/div[3]/ul/li[1]/div/form[1]/span[3]/input")))
    taoimg.send_keys(r"/home/hj/문서/GitHub/dino/a.png")

    time.sleep(1)

    html = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[1]/td/div[1]/a[2]")))
    html.click()

    time.sleep(1)

    tabs = driver.window_handles

    driver.switch_to.window(tabs[1])

    time.sleep(1)

    driver.maximize_window()

    time.sleep(1)

    html = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"textarea-editor\"]")))
    html.send_keys("<div>1111111</div>")

    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/div[3]/button[1]")))
    done.click()

    time.sleep(1)
    driver.switch_to.window(tabs[0])
    driver.switch_to.frame("ifm_TDM395")
    time.sleep(1)


    tak = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td/div/label[1]")))
    tak.click()

    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"selShipmentPlaceNo\"]")))
    done.click()

    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/table/tbody/tr[4]/td/div/table/tbody/tr[5]/td/select/option[2]")))
    done.click()

    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"selBundleDeliveryTemp\"]")))
    done.click()
    
    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/table/tbody/tr[4]/td/div/table/tbody/tr[5]/td/div[2]/div/div[1]/select/option[2]")))
    done.click()

    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[5]/a[3]")))
    done.click()

    time.sleep(5)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[5]/a[3]")))
    done.click()

    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[5]/a[2]")))
    done.click()

    time.sleep(1)

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"lbConfirmForGoodsImage\"]")))
    done.click()

    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"lblConfirmForGoodsName\"]")))
    done.click()

    time.sleep(1)

    #done = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"lblConfirmForSellerDiscount\"]")))
    #done.click()

    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"lblConfirmForGoodsPrice\"]")))
    done.click()

    time.sleep(1)

    done = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"btnConfirm\"]")))
    done.click()

    time.sleep(1)
    driver.switch_to.window(tabs[0])
    time.sleep(1)

    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass

    # alert 클릭 해야함!

    time.sleep(1)

    driver.close()

def cupload():
    payload = {
        "sellerProductName": "향수",
        "vendorId": "판매자 id",
        "saleStartedAt": "시작일시",
        "saleEndedAt": "종료일시",
        "deliveryMethod": "AGENT_BUY", # 배송 타입
        "deliveryCompanyCode": "택배사 코드",
        "deliveryChargeType": "NOT_FREE", # 배송비 타입
        "deliveryCharge": "2000", # 배송비
        "freeShipOverAmount": "100000", # 무료 배송을 위한 최소 배송비
        "deliveryChargeOnReturn": "2000", # 무료배송인 경우 환불할때 구매자가 지불하는 비용
        "remoteAreaDeliverable": "N", # 도서산간 지역 배송 여부
        "unionDeliveryType": "UNION_DELIVERY", # 묶음 배송 여부
        "returnCenterCode": "NO_RETURN_CENTERCODE", # 반품지센터 코드
        "returnChargeName": "0", # 반품지 명
        "companyContactNumber": "0", # 반품지 연락처
        "returnZipCode": "0", # 반품지 zip코드
        "returnAddress": "0", # 반품지 주소
        "returnAddressDetail": "0", # 반품지주소 상세
        "returnCharge": "2000", # 반품 배송비
        "outboundShippingPlaceCode": "출고지 주소코드", # 출고지 주소 코드 구매대행은 해외주소지입력
        "vendorUserId": "사용자id", # 쿠팡 사용자 아이디
        "requested": "false", # 자동 승인 요청 여부
        "items": [
            {
                "itemName": "상품명", # 상품옵션명
                "originalPrice": "정가", # 정가
                "salePrice": "할인가", # 할인가
                "maximumBuyCount": "9999", # 재고 수량
                "maximumBuyForPerson": "0", # 1인당 최대 구매 가능 수량
                "maximumBuyForPersonPeriod": "1", # 1인당 재구매 가능한 기간
                "outboundShippingTimeDay": "1", # 출고 예정일
                "unitCount": "0", # 단위수량, 상관없음
                "adultOnly": "false", # 성인 전용 상품 여부
                "taxType":  "FREE", # 과세 여부
                "parallelImported": "NOT_PARALLEL_IMPORTED", # 병행 수입 여부
                "overseasPurchased": "OVERSEAS_PURCHASED", # 구매 대행 여부
                "pccNeeded": "true" # PCC 필수 입력 여부
            }
        ],
        "images": [

            {
                "imageOrder": "0,1,2...", # 이미지 순서
                "imageType": "REPRESENTATION", # 혹은 DETAIL 이미지 타입을 의미함
                "vendorPath": "http" # 이미지 링크
            }
        ],
        "attributes": [
            {
                "attributeTypeName": "타입명", # 옵션 타입명
                "attributeValueName": "옵션명" # 옵션명
            }
        ],
        "contents":[
            {
                "contentsType": "IMAGE", # 콘텐츠 타입
                "contentDetails":[
                    {
                        "content": "내용", # 콘텐츠 내용
                        "detailType": "IMAGE" # 세부타입
                    }
                ]
            }
        ]
    }

    print(requests.post("https://api-gateway.coupang.com/v2/providers/seller_api/apis/api/v1/marketplace/seller-products", json=payload).json())

def lotupload():
    payload = {
        "spdLst": [
            {
                "trGrpCd": "SR",
                "trNo": "LO10xxxxx",
                "lrtrNo": "",
                "purTrNo": "",
                "scatNo": "BC63080300",
                "dcatLst": [
                    {
                        "mallCd": "LTON",
                        "lfDcatNo": "FC11130203"
                    }
                ],
                "epdNo": "A00000016",
                "slTypCd": "GNRL",
                "pdTypCd": "GNRL_GNRL",
                "spdNm": "유성민_상품등록테스트",
                "brdNo": "P306",
                "mfcrNm": "테스트제조사",
                "oplcCd": "KR",
                "mdlNo": "테스트모델번호",
                "barCd": "123123",
                "tdfDvsCd": "01",
                "slStrtDttm": "20200131000000",
                "slEndDttm": "20221231235959",
                "pdItmsInfo": {
                    "pdItmsCd": "06",
                    "pdItmsArtlLst": [
                        {
                            "pdArtlCd": "0020",
                            "pdArtlCnts": "색상입력값"
                        },
                        {
                            "pdArtlCd": "0060",
                            "pdArtlCnts": "제조국입력"
                        },
                        {
                            "pdArtlCd": "0070",
                            "pdArtlCnts": "제조자입력"
                        },
                        {
                            "pdArtlCd": "0080",
                            "pdArtlCnts": "품질보증기준입력"
                        },
                        {
                            "pdArtlCd": "0090",
                            "pdArtlCnts": "책임자입력"
                        },
                        {
                            "pdArtlCd": "0140",
                            "pdArtlCnts": "크기입력"
                        },
                        {
                            "pdArtlCd": "0160",
                            "pdArtlCnts": "품명입력"
                        },
                        {
                            "pdArtlCd": "0170",
                            "pdArtlCnts": "주요 소재 입력"
                        },
                        {
                            "pdArtlCd": "0180",
                            "pdArtlCnts": "구성품입력"
                        },
                        {
                            "pdArtlCd": "0190",
                            "pdArtlCnts": "배송설치비용입력"
                        },
                        {
                            "pdArtlCd": "0200",
                            "pdArtlCnts": "Y"
                        }
                    ]
                },
                "sftyAthnLst": [
                    {
                        "sftyAthnTypCd": "LIFE_SUPS",
                        "sftyAthnOrgnNm": "[방송통신기자재]적합등록",
                        "sftyAthnNo": "1241251251"
                    }
                ],
                "scatAttrLst": [
                    {
                        "optCd": "10594",
                        "optNm": "커튼 재질",
                        "optValCd": "104170",
                        "optVal": "레이스"
                    },
                    {
                        "optCd": "11330",
                        "optNm": "패턴/프린트",
                        "optValCd": "109638",
                        "optVal": "단색(무지)"
                    },
                    {
                        "optCd": "11582",
                        "optNm": "캐노피 형태",
                        "optValCd": "110544",
                        "optVal": "사각형"
                    }
                ],
                "purPsbQtyInfo": {
                    "itmByMinPurYn": "Y",
                    "itmByMinPurQty": 2,
                    "itmByMaxPurPsbQtyYn": "Y",
                    "maxPurQty": 1000
                },
                "ageLmtCd": "0",
                "prstPsbYn": "N",
                "prstPckPsbYn": "N",
                "prstMsgPsbYn": "N",
                "prcCmprEpsrYn": "N",
                "bookCultCstDdctYn": "N",
                "isbnCd": "",
                "impDvsCd": "NONE",
                "cshbltyPdYn": "N",
                "gftvShpCd": "",
                "dnDvPdYn": "N",
                "toysPdYn": "N",
                "intgSlPdNo": "",
                "nmlPdYn": "N",
                "prmmPdYn": "N",
                "otltPdYn": "N",
                "prmmInstPdYn": "N",
                "brkHmapPkcpPsbYn": "N",
                "mvCmcoCd": "",
                "ctrtTypCd": "A",
                "pdSzInfo": {
                    "pdWdthSz": "100",
                    "pdLnthSz": "200",
                    "pdHghtSz": "300",
                    "pckWdthSz": "110",
                    "pckLnthSz": "210",
                    "pckHghtSz": "310"
                },
                "pdStatCd": "NEW",
                "dpYn": "Y",
                "ltonDpYn": "Y",
                "scKwdLst": [
                    "검색키워드1",
                    "검색키워드2",
                    "검색키워드3"
                ],
                "pdFileLst": [
                    {
                        "fileTypCd": "PD",
                        "fileDvsCd": "WDTH",
                        "origFileNm": "https://image.ellotte.com/ellt.static.lotteeps.com/goods/img/95/53/78/07/10/1007785395_mast.jpg"
                    },
                    {
                        "fileTypCd": "PD",
                        "fileDvsCd": "VDO_URL",
                        "origFileNm": "https://simage.lottemart.com/lim/static_root/images/prodimg/video/88094/3379/8809433791613.mp4"
                    }
                ],
                "epnLst": [
                    {
                        "pdEpnTypCd": "DSCRP",
                        "cnts": "<html>~~~</html>"
                    }
                ],
                "cnclPsbYn": "Y",
                "dmstOvsDvDvsCd": "DMST",
                "pstkYn": "N",
                "dvProcTypCd": "LO_ENTP",
                "dvPdTypCd": "GNRL",
                "sndBgtNday": "0",
                "sndBgtDdInfo": {
                    "nldySndCloseTm": "1300",
                    "satSndPsbYn": "Y",
                    "satSndCloseTm": "1200"
                },
                "dvRgsprGrpCd": "GN101",
                "dvMnsCd": "DPCL",
                "owhpNo": "115",
                "hdcCd": "0001",
                "dvCstPolNo": "335",
                "adtnDvCstPolNo": "",
                "cmbnDvPsbYn": "Y",
                "dvCstStdQty": 0,
                "qckDvUseYn": "Y",
                "crdayDvPsbYn": "N",
                "hpDdDvPsbYn": "N",
                "saveTypCd": "NONE",
                "shopCnvMsgPsbYn": "N",
                "rgnLmtPdYn": "N",
                "fprdDvPsbYn": "N",
                "spcfSqncPdYn": "N",
                "rtngPsbYn": "N",
                "xchgPsbYn": "Y",
                "echgPsbYn": "N",
                "cmbnRtngPsbYn": "Y",
                "rtngHdcCd": "0001",
                "rtngRtrvPsbYn": "Y",
                "rtrvTypCd": "ENTP_RTRV",
                "rtrpNo": "115",
                "stkMgtYn": "Y",
                "sitmYn": "Y",
                "optSrtLst": [
                    {
                        "optSeq": 1,
                        "optNm": "색상",
                        "optValSrtLst": [
                            {
                                "optValSeq": 1,
                                "optVal": "맛있는초코색"
                            }
                        ]
                    }
                ],
                "itmLst": [
                    {
                        "eitmNo": "ITM_1",
                        "dpYn": "Y",
                        "sortSeq": 1,
                        "itmOptLst": [
                            {
                                "optNm": "색상",
                                "optVal": "맛있는초코색"
                            }
                        ],
                        "itmImgLst": [
                            {
                                "epsrTypCd": "IMG",
                                "epsrTypDtlCd": "IMG_SQRE",
                                "origImgFileNm": "https://image.ellotte.com/ellt.static.lotteeps.com/goods/img/95/53/78/07/10/1007785395_mast.jpg",
                                "rprtImgYn": "Y"
                            },
                            {
                                "epsrTypCd": "IMG",
                                "epsrTypDtlCd": "IMG_SQRE",
                                "origImgFileNm": "https://image.ellotte.com/ellt.static.lotteeps.com/goods/img/95/53/78/07/10/1007785395_mast.jpg",
                                "rprtImgYn": "N"
                            }
                        ],
                        "pdUtStdInfo": {
                            "pdCapa": 10
                        },
                        "slPrc": 200000,
                        "stkQty": 110
                    }
                ],
                "adtnPdYn": "Y",
                "adtnPdInfo": {
                    "sortCd": "NAME_ASC",
                    "adtnTypeLst": [
                        {
                            "adtnTypNm": "추가유형명입니다.",
                            "epsrPrirRnkg": 11,
                            "adtnPdLst": [
                                {
                                    "adtnPdNm": "이름입니다",
                                    "epdNo": "YSM_ADTN_NUMBER",
                                    "epsrPrirRnkg": 12,
                                    "slPrc": 1700,
                                    "stkQty": 1203,
                                    "useYn": "Y"
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }


def oneupload():
    pass