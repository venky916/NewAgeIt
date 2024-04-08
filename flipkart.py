from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains

import time

service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)

driver.get("https://flipkart.com")
print(driver)

# element1=driver.find_element(By.PARTIAL_LINK_TEXT,"Login")
# element1.click()

# element2=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
# print(element2)
# element2.send_keys("9494600916"+Keys.ENTER)
# time.sleep(5) 

element3=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
element3.send_keys("shoes"+Keys.ENTER)
# Find the element using CSS selector
# element4=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a')
element4=driver.find_element(By.CLASS_NAME,"_2r_T1I") #worked

# element4 = driver.find_element(By.XPATH,'//*[@data-id="SHOG7H6QYEAGZQHY"]') not worked
# element4 = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div/form') not worked
# Get the text of the element
# print(element4)
# text = element4.text
# print("hello",text)
# print()
# # Get the value of a specific attribute (e.g., href)
# href_value = element4.get_attribute("href")
# print("hi",href_value)
# child_elements = element.find_elements(By.CLASS_NAME, "_2UzuFa")

element4.click()
# Scroll to the element
# driver.execute_script("arguments[0].scrollIntoView();", element4)

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Adjust the timeout as needed

windows = driver.window_handles
driver.switch_to.window(windows[1]) 

# Find child elements within the main element

# element5=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button')
element5=driver.find_element(By.CLASS_NAME,'_2KpZ6l _2U9uOA _3v1-ww')
element5.click()

time.sleep(10) 