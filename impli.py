# import webdriver 
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
# create webdriver object 
driver = webdriver.Chrome() 
	
# set implicit wait time 
driver.implicitly_wait(100) # seconds 

# get geeksforgeeks.org 
driver.get("https://www.geeksforgeeks.org/") 
	
# get element after 10 seconds 
element = driver.find_element(By.PARTIAL_LINK_TEXT,"Courses") 
print(element)
# click element 
element.click() 
time.sleep(100)
