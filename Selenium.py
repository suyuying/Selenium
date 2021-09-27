#Selenium是一個瀏覽器自動化的套件(Package)，可以利用Python撰寫自動化的腳本來執行各種網站
import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-notifications")
chrome = webdriver.Chrome('./chromedriver')
chrome.get("https://www.facebook.com")
email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")
email.send_keys("")
password.send_keys("")

password.submit()
for x in range(1, 5):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)


