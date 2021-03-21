from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

op = webdriver.ChromeOptions()
op.add_argument("headless")

def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

id = '네이버 아이디'
pw = '네이버 비번'

driver = webdriver.Chrome("D:\chromedriver_win32/chromedriver.exe")
driver.get('https://sports.news.naver.com/gameCenter/textRelay.nhn?category=kbo&gameId=20210322WOSS02021')

driver.find_element_by_xpath('//*[@class="gnb_one"]/ul/li/a').click()
time.sleep(1)
copy_input('//*[@id="id"]', id)
time.sleep(1)
copy_input('//*[@id="pw"]', pw)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)
while True:
    driver.find_element_by_xpath('//*[@class="_reactionModule u_likeit"]/ul/li/a').click()
