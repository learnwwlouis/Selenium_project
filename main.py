from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

http_username = "Louis_FW"
http_password = "00000000"
def main():
    # Login
    try:
        driver.get('http://www.asusrouter.com/')
        time.sleep(5)
        element1 = driver.find_element("xpath", "//*[@id=\"login_username\"]")
        time.sleep(5)
        print(element1)
        element1 = driver.find_element("xpath", "//*[@id=\"login_username\"]")
        element1.send_keys(http_username);
        element2 = driver.find_element("xpath", "//*[@name=\"login_passwd\"]")
        element2.send_keys(http_password);
        time.sleep(5)
        try:
            driver.find_element("xpath", "//div[@onclick=\"login();\"]").click()
        except:
            print("Do not find login(); try preLogin();")
            try:
                driver.find_element("xpath", "//div[@onclick=\"preLogin();\"]").click()
            except:
                print("Can not find Login element!")

    except TimeoutError:
        driver.quit()


if __name__ == "__main__":
    main()
