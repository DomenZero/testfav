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
		

		url_list0 = []
		html_page = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html_page, "lxml")
		for id_1 in soup.find_all("a", {"class": "result-title hdrlnk"}):
		 	# print(id_1["data-id"])
		 	url_list0.append(id_1["data-id"])
# print the first element id 
		print("First element: "+url_list0[0]) 

# Click favorites
		# driver.find_element_by_xpath("//span[@role='button'][@title='save this post in your favorites list']").click()

		# aa=driver.find_elements_by_xpath("//div[@class='favorites']//a[@href]")
		# for a in aa:
		# 	linkk=a.get_attribute("href")
		# 	print(a.get_attribute("href"))

	
		aa1=driver.find_elements_by_xpath("//li[@class='result-row fav']")
		for a1 in aa1:
			if (url_list0[0]==a1.get_attribute("data-pid")):
				print("First post is favorites: "+ a1.get_attribute("data-pid"))
			else:
				print("First post isn't favorites")

	def tear_down(self):
		self.driver.quit()
 
if __name__ == "__main__":
	unittest.main()
