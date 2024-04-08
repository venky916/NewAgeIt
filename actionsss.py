from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.action_chains import ActionChains

service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)


# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
  
# get element 
element = driver.find_element(By.PARTIAL_LINK_TEXT,"DSA")

# get target element  
# target_element = driver.find_element(By.PARTIAL_LINK_TEXT,"Hard") 

# create action chain object
action = ActionChains(driver)

#  and drop the item 
# action.drag_and_drop(source_element, target_element) 

 # perform the operation
# action.perform()
# create action chain object
# action = ActionChains(driver)

# action.click_and_hold(on_element = element)
# perform the operation
# action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# move the cursor 
# action.move_by_offset(200, 200)
# action.perform()
# action.move_to_element(element).click().perform() 
# action.move_to_element_with_offset(element, 200, 200).click().perform() 
   
# create action chain object 
# action = ActionChains(driver) 
  
# click the item 
# action.click(on_element = element) 
  
# # perform the operation 
# action.perform() 
  
# # get another element  
# another_element = driver.find_element(By.PARTIAL_LINK_TEXT,"Course")
  
# # reset the action 
# action.reset_actions() 
  
# # click the item 
# action.click(on_element = another_element) 
  
# # perform the operation 
# action.perform()


# get element  
element = driver.find_element(By.CLASS_NAME,"ant-input-lg")  
print(element)
# click the item 
action.click(on_element = element) 
  
# send keys 
action.send_keys("Arrays") 
# search_element=driver.find_element(By.TAG_NAME,"span")
search_element=driver.find_element(By.CLASS_NAME,"ant-input-search-button")
action.click(on_element = search_element)
# perform the operation 
action.perform() 

time.sleep(10)