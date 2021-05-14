from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import userSettings
import mtgSettings


driver=webdriver.Chrome('./chromedriver')

driver.get('https:\\www.17lands.com\login')

usernameSelector = 'email'
passwordSelector = 'password'

currentSelector = driver.find_element_by_name(usernameSelector)
currentSelector.clear()
currentSelector.send_keys(userSettings.username17)