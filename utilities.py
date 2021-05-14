from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import userSettings
import mtgSettings

def startBrowser():
    driver=webdriver.Chrome('./chromedriver')
    return driver

def login(driver):
    driver.get('https:\\www.17lands.com\login')

    usernameSelector = 'email'
    passwordSelector = 'password'
    loginSelector = 'submit'

    currentSelector = driver.find_element_by_name(usernameSelector)
    currentSelector.clear()
    currentSelector.send_keys(userSettings.username17)

    currentSelector = driver.find_element_by_name(passwordSelector)
    currentSelector.clear()
    currentSelector.send_keys(userSettings.password17)

    currentSelector = driver.find_element_by_name(loginSelector)
    currentSelector.click()

    return driver