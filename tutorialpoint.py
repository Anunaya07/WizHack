from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

query = input()

PATH = "C:\\Users\\Happy\\Downloads\\chromedriver_win32\\chromedriver.exe"
# create webdriver object
driver = webdriver.Chrome(PATH)
driver.get("https://www.tutorialspoint.com/index.htm/")

searchButton = driver.find_element_by_name('search')
searchButton.click()

inputField = driver.find_element_by_name('search')
inputField.click()

inputField.send_keys(query)
inputField.send_keys(Keys.ENTER)
