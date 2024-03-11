import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

def sleep():
    time.sleep(0.5)

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.maximize_window()

# go to TAU personal info
driver.get('https://www.ims.tau.ac.il/Tal/Sys/Main.aspx?id=315852608&src=&sys=tal&rightmj=1&dt=08092022193314')
sleep()  
# eneter username
user_name = driver.find_element("name", "txtUser")
user_name.send_keys("########## INSERT USERNAME ##############") ########################### insert  username
print(user_name)
# enter id
id = driver.find_element("name", "txtId")
id.send_keys("##############INSERT ID ##############") ############################### insert id
# enter password
password = driver.find_element("name", "txtPass")
password.send_keys("############## INSERT PASS ##############") ############################### insert password 
# press submit
enter = driver.find_element("name", "enter")
enter.send_keys(Keys.RETURN)

sleep()
# press notebooks li
notebooks = driver.find_element("id" ,"li8")
notebooks.click()
sleep()

# press ishur
# click tab then enter on the page
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.RETURN)
actions.perform()

#driver.close()
