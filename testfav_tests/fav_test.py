import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request


class FavTest(unittest.TestCase):
	# def __init__(self, driver):
	#     self.driver = driver

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
		self.url = "https://sfbay.craigslist.org/d/jobs/search/jjj"
		# self.driver=webdriver.Chrome(chrome_options=chrome_options)
		# self.driver.maximize_window()
		self.driver.implicitly_wait(20)
		# self.delay = 3

	def test_urls_1(self):
		driver=self.driver
		driver.get("https://sfbay.craigslist.org/d/jobs/search/jjj")
		# driver.get("http://econpy.pythonanywhere.com/ex/001.html")
		# data_id=driver.find_element_by_id("sortable-results")
		# data_id = driver.find_element_by_xpath("//div[@title='buyer-name']")
		# data_id = driver.find_element_by_xpath("//li[@class='result-info']")

		# data_id = driver.find_element_by_xpath("//*[@id="sortable-results"]/ul/li[1]/p/a").click()

		# //*[@id="page-top"]/header[1]/div/ul[2]/li[1]/div/a
		# data_id = driver.find_element_by_xpath("//*[@id="page-top"]/header[1]/div/ul[2]/li[1]/div/a")
		# result-title hdrlnk
		# print name
		# posts=driver.find_element_by_class_name("hdrlnk")

		# posts=driver.find_element_by_class_name("result-info")

		# //*[@id="sortable-results"]/ul/li[1]/p/span[1]
		# if driver.find_all('span',{'class':'icon icon-star fav'}) != None:
		# id = element.get_attribute("id")
		# data_fav=driver.find_element_by_class_name("icon-star").click()
		# driver.find_element_by_css_selector('.icon.icon-star').click()

		# click favorites star 
		

		url_list0 = []
		html_page = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html_page, "lxml")
		for id_1 in soup.find_all("a", {"class": "result-title hdrlnk"}):
		 	# print(id_1["data-id"])
		 	url_list0.append(id_1["data-id"])
# print the first elemnt id 
		print("bala: "+url_list0[0]) 


		driver.find_element_by_xpath("//span[@role='button'][@title='save this post in your favorites list']").click()

		# click favorites
		aa=driver.find_elements_by_xpath("//div[@class='favorites']//a[@href]")
		for a in aa:
			linkk=a.get_attribute("href")
			print(a.get_attribute("href"))

		driver.find_element_by_xpath("//div[@class='favorites']").click()
		



		# open link
		# data_id = driver.find_element_by_class_name("hdrlnk").click()
# link favorite from 2 page
		url_list = []
		html_page = urllib.request.urlopen(linkk)
		soup = BeautifulSoup(html_page, "lxml")
		for id_2 in soup.find_all("a", {"class": "result-title hdrlnk"}):
		 	# print(id_1["data-id"])
		 	url_list.append(id_2["data-id"])
# print the first elemnt id 
		print(url_list[0]) 


		# print(posts.text)
		# data_id = driver.find_element_by_xpath("//*[@id="sortable-results"]/ul/li[1]/p/a").click()
		# for post in posts:
		



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
