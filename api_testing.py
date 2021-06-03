from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
import postman555



driver = webdriver.Chrome()
driver.get('https://www.flickr.com/services/api/explore/flickr.photos.getPopular')


sign_in = driver.find_element_by_xpath('//*[@id="gn-wrap"]/div[3]/ul/li[2]/a/span').click()
time.sleep(3)
email = driver.find_element_by_xpath('//*[@id="login-email"]')
email.send_keys('retinanisaichandu@gmail.com')
next = driver.find_element_by_xpath('//*[@id="login-form"]/button/span').click()
time.sleep(2)
actions = ActionChains(driver)
actions.send_keys('626462646264')
actions.perform()
sign_in_enter = driver.find_element_by_xpath('//*[@id="login-form"]/button/span').click()
time.sleep(7)

api_key = driver.find_element_by_xpath('//*[@id="param_api_key"]')

api_key.send_keys('145bce6d066c73ffd4292033d33c3180')
user_id = driver.find_element_by_xpath('//*[@id="param_user_id"]')
user_id.send_keys('193139599@N07')

select = Select(driver.find_element_by_name('format'))
select.select_by_visible_text('JSON')
time.sleep(5)

radio  = driver.find_element_by_xpath('//*[@id="nosign"]')
driver.execute_script('arguments[0].click();',radio)

call_method = driver.find_element_by_xpath('/html/body/div[2]/table[2]/tbody/tr/td[1]/form/input[3]')
driver.execute_script('arguments[0].click();',call_method)

postman555.main()

