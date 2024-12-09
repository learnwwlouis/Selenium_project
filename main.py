#導入webdriver​
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#建立一個chrome的webdriver
driver = webdriver.Chrome()


driver.get("http://www.asusrouter.com/index.asp")

#防止網頁馬上開了就關，再執行一次檔案就可以關閉頁面
input()
