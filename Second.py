from selenium import webdriver	

# For using sleep function because selenium
# works only when the all the elements of the
# page is loaded.
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# Creating an instance webdriver
browser = webdriver.Chrome('D:/Compressed/chromedriver_win32_2/chromedriver.exe')
browser.get('http://127.0.0.1:8000/')

browser.maximize_window()
browser.find_element(By.ID, "home").click()

# movie page
browser.find_element(By.LINK_TEXT, "Movies").click()
time.sleep(5)

# Pages - blog details
browser.find_element_by_xpath('//*[@id="primary-menu"]/li[6]/a').click()
browser.find_element_by_xpath('//*[@id="primary-menu"]/li[6]/ul/li/a').click()
time.sleep(3)

# login
browser.find_element(By.LINK_TEXT, "Login").click()
elem = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[3]/div/form/div[1]/input')
elem.send_keys('user')
elem = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[3]/div/form/div[2]/input')
elem.send_keys('password')
time.sleep(5)
browser.find_element_by_xpath('/html/body/div/div/div[2]/div[3]/div/form/div[3]/div[2]/button').click()

# ticket
browser.find_element(By.LINK_TEXT, "Tickets").click()
time.sleep(5)
browser.find_element_by_xpath('/html/body/div[3]/div/div/a').click()

# trailer
browser.find_element_by_xpath('/html/body/section[3]/div/div[2]/div[2]/div/div[2]/div/a/i').click()
time.sleep(5)
browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/button').click()

# close
browser.close()