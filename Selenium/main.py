from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import random

browser = webdriver.Chrome(executable_path=r"D:\Users\Henry\Downloads\github\Learning-Python\Selenium\chromedriver.exe")

login = 'https://farmrpg.com/index.php#!/login.php'

browser.get(login)
time.sleep(1)
browser.find_element(By.NAME, "username").send_keys("a11tvvvf")
browser.find_element(By.NAME, "password").send_keys("test1234")
browser.find_element(By.CSS_SELECTOR, 'input#login_sub.button.btngreen').click()

def Farming():
    browser.get('https://farmrpg.com/index.php#!/xfarm.php?id=245078')
    seeds = browser.find_elements_by_xpath('//*[@id="fireworks"]/div[2]/div[2]/div/div[2]/div[3]/div/div/ul/li/a/div/div/div[2]/select/option')
    for seed in seeds:
        if seed.text == 'Out of seeds...':
            print("out of seeds, buying seeds")           
    
def PlantAll():
    browser.find_element(By.CLASS_NAME,"plantallbtn").click()
    time.sleep(1)
    browser.find_elements(By.CLASS_NAME, "actions-modal-button")[0].click()

def HarvestAll():
    browser.find_element(By.CLASS_NAME,"harvestallbtn").click()
    time.sleep(1)
    

browser.find_element(By.CLASS_NAME,"c-progress-bar-fill").get_attribute("style") == 'width: 100%;'


def Fishing():
    browser.get('https://farmrpg.com/index.php#!/fishing.php?id=1')
    try:
        worms = int(browser.find_element(By.CLASS_NAME, "col-45").find_element(By.TAG_NAME,'strong').text)
    except:
        Fishing()
    while worms > 0:
        Catch()
        worms = int(browser.find_element(By.CLASS_NAME, "col-45").find_element(By.TAG_NAME,'strong').text)
    if worms == 0:
        BuyWorms()


def BuyWorms():
    market = 'https://farmrpg.com/index.php#!/store.php'
    browser.get(market)
    time.sleep(1)
    try:
        browser.find_elements(By.CLASS_NAME, "maxqty")[-1].click()
    except:
        browser.get(market)
    time.sleep(.5)
    s= browser.find_elements(By.CLASS_NAME, "buybtn")[-1]
    browser.execute_script("arguments[0].click();", s)
    time.sleep(.5)
    browser.find_elements(By.CLASS_NAME, "actions-modal-button")[0].click()
    time.sleep(.5)
    browser.find_elements(By.CLASS_NAME, "modal-button")[2].click()
    Fishing()

def sellAll():
    browser.get('https://farmrpg.com/index.php#!/market.php')
    time.sleep(.5)
    browser.find_elements(By.CLASS_NAME, "sellallbtn")[0].click()
    time.sleep(.5)
    browser.find_elements(By.CLASS_NAME, "actions-modal-button")[0].click()
    time.sleep(.5)
    browser.find_elements(By.CLASS_NAME, "modal-button")[0].click()



def Catch():
    fish = browser.find_elements(By.CLASS_NAME, "fishcell")
    catcher = browser.find_elements(By.CLASS_NAME, "fishcaught")
    for i in fish:
        try:
            i.click()
        except:
            pass
    for k in catcher:
        try:
            time.sleep(.5)
            k.click()
            time.sleep(1)
        except:
            pass