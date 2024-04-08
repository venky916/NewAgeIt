# import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.by import By

import time
# create webdriver object 
driver = webdriver.Chrome() 

# # get geeksforgeeks.org 
driver.get("https://www.geeksforgeeks.org/") 

# # add_cookie method driver 
# driver.add_cookie({"name" : "foo", "value" : "bar"}) 

# time.sleep(100)

# get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/")

# # get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/explore")

# # one step back in browser history
# driver.back()
# driver.close()

element = driver.find_element(By.PARTIAL_LINK_TEXT,"Courses") 
  
# # get id of element 
# id = element._id 
# print("hell",element._id)
# # create another element 
# element_clone = driver.create_web_element(id) 

# print("*",element_clone)

time.sleep(100)