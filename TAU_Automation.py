import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

def sleep():
    time.sleep(0.5)

directory = os.getcwd()
path = directory + "\chromedriver.exe"
print(path)

driver = webdriver.Chrome(path)
driver.maximize_window()

# go to TAU personal info
driver.get('https://www.ims.tau.ac.il/Tal/Sys/Main.aspx?id=315852608&src=&sys=tal&rightmj=1&dt=08092022193314')
sleep()
# eneter username
user_name = driver.find_element_by_name("txtUser")
user_name.send_keys("insert  username") ########################### insert  username
# enter id
id = driver.find_element_by_name("txtId")
id.send_keys("insert id") ############################### insert id
# enter password
password = driver.find_element_by_name("txtPass")
password.send_keys("insert password") ############################### insert password
# press submit
enter = driver.find_element_by_name("enter")
enter.send_keys(Keys.RETURN)

sleep()
# press notebooks li
notebooks = driver.find_element_by_id("li7")
notebooks.click()
sleep()

# press ishur
# click tab then enter on the page
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.RETURN)
actions.perform()

sleep()

# semster B
actions = ActionChains(driver)

actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.RETURN)
actions.perform()
sleep()



#time.sleep()
#driver.close()
