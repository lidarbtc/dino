from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random

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
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://wpartner.wemakeprice.com/login")
    wait = WebDriverWait(driver, 10)
    rd = random.randrange(1,9999999)

    time.sleep(2)

    with open('./{}.png'.format(rd), 'wb') as file:
        file.write(driver.find_element(By.XPATH, '//*[@id="_captchaImage"]').screenshot_as_png)

    driver.close()
    
while True:
    wpupload(1,1,1000,1000,1000,1000)