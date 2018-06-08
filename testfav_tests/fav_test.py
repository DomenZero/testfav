import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FavTest(unittest.TestCase):
	# def __init__(self, driver):
	#     self.driver = driver

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
		# self.driver=webdriver.Chrome(chrome_options=chrome_options)
		# self.driver.maximize_window()
		self.driver.implicitly_wait(10)

	def test_user_login(self):
		driver=self.driver
		driver.get("https://sfbay.craigslist.org/d/jobs/search/jjjj")
		# driver.get("http://econpy.pythonanywhere.com/ex/001.html")
		# data_id=driver.find_element_by_id("sortable-results")
		# data_id = driver.find_element_by_xpath("//div[@title='buyer-name']")
		data_id = driver.find_element_by_xpath("//li[@class='result-info']")
		print(data_id.text)



		# driver.get("https://mail.ukr.net/desktop/login")
		# login_field=driver.find_element_by_id("id-1")
		# login_field.send_keys("autotestorgua")
		# password_field = driver.find_element_by_id("id-2")
		# password_field.send_keys("testpass")
		# button_login = driver.find_element_by_xpath("//*[text()='Увійти']")
		# button_login.click()
		# user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
		# assert user_mail.text == "au"
		# example 2
		# driver=self.driver
		# driver.get("http://www.python.org")
		# self.assertIn("Python",driver.title)
		# elem=driver.find_element_by_name("q")
		# elem.send_keys("selenium")
		# elem.send_keys(Keys.RETURN)
		# self.assertIn("Google",driver.title)

		# self.driver = driver
		# driver = self.driver
		# driver.get("https://mail.ukr.net/desktop/login")
		# login_field = driver.find_element_by_id("id-1")
		# login_field.send_keys("autotestorgua")
		# password_field = driver.find_element_by_id("id-2")
		# password_field.send_keys("testpass")
		# button_login = driver.find_element_by_xpath("//*[text()='Увійти']")
		# button_login.click()
		# user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
		# assert user_mail.text == "au"

	def tear_down(self):
		self.driver.quit()
 
if __name__ == "__main__":
	# suite=unittest.defaultTestLoader.loadTestsFromTestCase(FavTest)
	# unittest.TextTestRunner().run(suite)

	# suite=unittest.TestSuite()
	# suite.addTest(FavTest('test_user_login'))
	# unittest.TextTestRunner().run(suite)

	unittest.main()
