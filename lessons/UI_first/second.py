from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://developer.mozilla.org')
search_locator = (By.CSS_SELECTOR, '#home-q')
search = driver.find_element(*search_locator)
search.send_keys('import')
search.send_keys(Keys.ENTER)
link = driver.find_element_by_css_selector('.result-3 .search-meta a')
link.send_keys(Keys.ENTER)
search_icon_locator = (By.CSS_SELECTOR, '.nav-main-search i.icon-search')
search_icon = driver.find_element(*search_icon_locator)
search_icon.click()
main_search_locator = (By.ID, 'main-q')
main_search = driver.find_element(*main_search_locator)
main_search.send_keys('blablabla')
main_search.clear()
main_search.send_keys('classes')
main_search.submit()

print(driver.title)
#qmic
#submit
#driver.quit()