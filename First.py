from selenium import webdriver	

# For using sleep function because selenium
# works only when the all the elements of the
# page is loaded.
import time

from selenium.webdriver.common.keys import Keys

# Creating an instance webdriver
browser = webdriver.Chrome('D:/Compressed/chromedriver_win32_2/chromedriver.exe')
browser.get('http://127.0.0.1:8000')

browser.maximize_window()

# venom trailer
browser.find_element_by_xpath('/html/body/section[3]/div/div[2]/div[1]/div/a/i').click()

#close trailer
time.sleep(4)
browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/button').click()

# back to top
time.sleep(4)
browser.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[2]/div/a').click()

#ticket button
time.sleep(4)
browser.find_element_by_xpath('//*[@id="primary-menu"]/li[7]/a').click()

#close ticket
time.sleep(4)
browser.find_element_by_xpath('/html/body/div[3]/div/div/a/i').click()

#open movies
time.sleep(4)
browser.find_element_by_xpath('//*[@id="primary-menu"]/li[2]/a').click()

#scroll The Page
time.sleep(4)
browser.execute_script("window.scrollTo(0,400 )")

#change spotlight 
time.sleep(3)
browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/div[2]/div/ul/li[2]').click()

#open team
time.sleep(4)
browser.find_element_by_xpath('//*[@id="primary-menu"]/li[3]/a').click()

time.sleep(4)
browser.execute_script("window.scrollTo(0,400 )")

#open IG
time.sleep(3)
browser.find_element_by_xpath('//*[@id="team"]/div/div[5]/div/div[2]/div/a[1]').click()

time.sleep(3)
browser.switch_to.window(browser.window_handles[1])
time.sleep(3)
browser.close()
browser.switch_to.window(browser.window_handles[0])  

time.sleep(4)
browser.close()