from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

logo_locator = (By.CSS_SELECTOR, 'a.logo')
logo = driver.find_element(*logo_locator)


driver.get('http://developer.mozilla.org')
#logo = driver.find_element_by_css_selector('#main-header div.center a.logo')

print(logo)
print(logo.text)

#import ipdb; ipdb.set_trace()

header = driver.find_element_by_id('main-header')
search = driver.find_element_by_class_name('q')

driver.quit()
