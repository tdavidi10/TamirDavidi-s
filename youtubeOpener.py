










from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#path = "C:\chromedriver.exe"
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.youtube.com')


#searching
search = driver.find_element_by_name("search_query")
search.send_keys("never gonna give you up")
time.sleep(1)
search.send_keys(Keys.RETURN)

#############
time.sleep(1)
#############
#clicking on video
video = driver.find_element_by_class_name("style-scope ytd-video-renderer")
time.sleep(2)
video.click()


time.sleep(200)








