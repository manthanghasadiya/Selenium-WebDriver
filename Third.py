from selenium import webdriver

# For using sleep function because selenium
# works only when the all the elements of the
# page is loaded.
import time

from selenium.webdriver.common.keys import Keys

# Creating an instance webdriver
browser = webdriver.Chrome("D:/Compressed/chromedriver_win32_2/chromedriver.exe")
browser.get("http://127.0.0.1:8000")

browser.maximize_window()

# venom trailer
elem = browser.find_element_by_name("Query")
elem.send_keys("Eternals")
elem.submit()
time.sleep(2)
browser.execute_script("window.scrollTo(0,1080 )")
# close trailer
time.sleep(3)

# back to top
time.sleep(3)
browser.find_element_by_xpath(
    "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/a/img"
).click()

browser.execute_script("window.scrollTo(0,580 )")


# ticket button
time.sleep(3)
browser.find_element_by_xpath(
    "//html/body/section[2]/div/div/div/div[2]/div/ul/li[9]/div[2]/a"
).click()


time.sleep(3)

browser.switch_to.window(browser.window_handles[0]) 



time.sleep(3)



browser.close()
browser.quit()