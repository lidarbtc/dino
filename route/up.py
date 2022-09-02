from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
from wcaptcha import captcha_predict
import time
import random
import os
import requests

def ssupload(nid, pw, taotitle, taoprice, taoqa, taocontent):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://sell.smartstore.naver.com/#/home/about")
    wait = WebDriverWait(driver, 10)

    login_form = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[2]/div[2]/div/div[1]/div[2]/button[1]/span")))
    login_form.click()

    username = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"login_id\"]")))
    password = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"password\"]")))

    username.send_keys("jnk-global@naver.com")
    time.sleep(2)
    password.send_keys("45396861Wns!")
    time.sleep(1)

    login = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/div/div[4]/div[3]/button")))
    login.click()

    time.sleep(2)

    driver.get("https://sell.smartstore.naver.com/#/products/create")

    title = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[7]/div/div[2]/div/div/div/div/div/div/input")))
    title.send_keys(taotitle)

    cate = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[2]/div/div/div[1]/input")))
    cate.send_keys("패")
    cate.send_keys(Keys.ENTER)

    price = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"prd_price2\"]")))
    price.send_keys(taoprice)

    qa = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"stock\"]")))
    qa.send_keys(taoqa)

    driver.execute_script("window.scrollTo(0, 2200)") 

    time.sleep(1)

    change = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[13]/div/div[2]/div/div/ncp-editor-form/div[1]/ul/li[2]/a")))
    change.click()

    content = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[13]/div/div[2]/div/div/ncp-editor-form/div[1]/div/div/textarea")))
    content.send_keys(taocontent)

    driver.execute_script("window.scrollTo(0, 1300)") 

    time.sleep(1)

    uploadimg = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[2]/fieldset/form/ng-include/ui-view[12]/div/ng-form/div[2]/div/div[1]/div/ncp-photo-infra-image-upload/div/div[1]/div/ul/li/div/a")))
    uploadimg.click()

    time.sleep(1)

    #taoimg1 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/button[1]")))
    #taoimg1.click()

    taoimg = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    taoimg.send_keys(r"/home/hj/문서/dino-20220823T080000Z-001/dino/a.png")

    time.sleep(2)

    upload = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div[3]/div[2]/div[1]/button[3]")))
    upload.click()

    time.sleep(3)

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
            with open('./wcaptcha/dataset/predict/{}.png'.format(rd), 'wb') as file:
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
                continue
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

    taoimg = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/form/div[12]/div[2]/div/table/tbody/tr[3]/td/div[3]/div[1]/label/label/input")))
    taoimg.send_keys(r"/home/hj/문서/GitHub/dino/a.png") # 오류

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

    up = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"setProdInfoBtn\"]")))
    up.click()

    time.sleep(1)

    driver.close()

def gupload(wid, pw, taotitle, taoprice, taoqa, taocontent):
    pass
    
for i in range(1, 3000):
    wpupload(1,1,1000,1000,1000,1000)