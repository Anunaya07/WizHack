from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

query = input()

PATH = "C:\\Users\\Happy\\Downloads\\chromedriver_win32\\chromedriver.exe"
# create webdriver object
driver = webdriver.Chrome(PATH)
driver.get("https://stackoverflow.com/")

searchButton = driver.find_element_by_name('q')
searchButton.click()



searchButton.send_keys(query)
searchButton.send_keys(Keys.ENTER)
