def main():
	from selenium import webdriver
	import time
	from selenium.webdriver.common.action_chains import ActionChains
	from selenium.webdriver.support.ui import Select
	driver = webdriver.Chrome()
	driver.get('https://web.postman.co/workspace/My-Workspace~26c63877-c876-4e20-8aeb-0bf2caf72f6b/request/create?requestId=7e430d9d-fbe8-4f8a-a759-18e5176d37a2')
	email = driver.find_element_by_xpath('//*[@id="username"]')
	email.send_keys('retinanisaichandu@gmail.com')
	password = driver.find_element_by_xpath('//*[@id="password"]')
	password.send_keys('Amrutha143')
	sign_in_button = driver.find_element_by_xpath('//*[@id="sign-in-btn"]').click()
	time.sleep(17)
	get_url = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div')

	get_url.send_keys('https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=145bce6d066c73ffd4292033d33c3180&user_id=193139599%40N07&format=json&nojsoncallback=1')
	send = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[6]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[1]')
	send.click()
	time.sleep(5)
	tests = driver.find_element_by_xpath('//*[@id="request-editor"]/div[1]/div/div[1]/div/div[6]/div/span').click()
	actions = ActionChains(driver)
	actions.send_keys('pm.test("Status code is 200", function () {pm.response.to.have.status(200);});')
	actions.perform()

	send.click()
	time.sleep(30)

if __name__ =='main':
	main()
	

