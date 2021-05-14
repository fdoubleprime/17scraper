import utilities
import selenium.webdriver.support.select as select

driver = utilities.startBrowser()
driver = utilities.login(driver)

expansionSelectorName = 'expansion'

driver.get('https://www.17lands.com/collection')

expansionSelector = select.Select(driver.find_element_by_name(expansionSelectorName))

expansionSelector.select_by_value('KHM')

driver.find_element_by_css_selector('#collection_app > div > div:nth-child(4) > table')