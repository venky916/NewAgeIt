from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.remote_connection import RemoteConnection

    
# Initialize custom driver instance
# driver = WebDriver()
#     # desired_capabilities=DesiredCapabilities.CHROME      


# driver.get("https://www.google.com")
# print(driver)
url="https://www.google.com"
conn=RemoteConnection(url,)
print(conn.browser_name)