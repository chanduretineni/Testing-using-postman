from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

hyperlink = "  https://www.atg.party/"
driver = webdriver.Chrome()
driver.get(hyperlink)
file = open("data.txt",'w')

 
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart
file.write("Back End:"+str(backendPerformance_calc)+'\n')
file.write("Front End:"+str(frontendPerformance_calc)+'\n')

print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)

 
login = driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/ul/li[2]/a').click()

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('wiz_saurabh@rediffmail.com ')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Pass@123')

sign_in = driver.find_element_by_xpath('//*[@id="frm_landing_page_user_login"]/div[3]/button').click()
time.sleep(10)

driver.get('https://www.atg.party/article')
time.sleep(5)

#cover_image = driver.find_element_by_id("add-cover-image").send_keys('/Users/retinenisaichandu/Desktop/cover_image.jpeg')

title = driver.find_element_by_xpath('//*[@id="title"]')
title.send_keys("Selenium")

info = driver.find_element_by_xpath('//*[@id="description"]/div/div[1]/div/div/div')

info.send_keys('Selenium is a portable framework for testing web applications. Selenium provides a playback tool for authoring functional tests without the need to learn a test scripting language')

post = driver.find_element_by_xpath('//*[@id="hpost_btn"]').click()

final_url = driver.current_url
print(final_url)
file.write(final_url)