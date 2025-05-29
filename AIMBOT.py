import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(2)
searchbox=driver.find_element(By.ID,"twotabsearchtextbox")
searchbox.click()
searchbox. send_keys("iphone")
searchbox. send_keys(Keys.RETURN)
time.sleep(3)
driver.execute_script("window.scrollTo(0,2000)")
lap=driver.find_elements(By.XPATH, "//button")
time.sleep(2)
if lap:
    laptop1=random.choice(lap)
    laptop1.click()
else:
    print("no response")
time.sleep(2)
cart1=driver.find_element(By.CLASS_NAME, "a-button-text").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"a-button-input").click()
time.sleep(3)
searchbox1=driver.find_element(By.ID, "ap_email_login")
searchbox1.send_keys("9094057729")
searchbox1.send_keys(Keys.RETURN)
time.sleep(2)
tt=driver.find_element(By.ID, "ap_password")
tt.send_keys("007")
tt.send_keys(Keys.RETURN)
time.sleep(2)