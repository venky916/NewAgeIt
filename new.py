


# URL of the Remote WebDriver server
# remote_server_addr = "http://<ip_address>:<port>/wd/hub"

# Desired capabilities for the browser
desired_capabilities = {
    "browserName": "chrome",
    "version": "latest",
    "platform": "WINDOWS"
}
# desired_capabilities=desired_capabilities
# driver = webdriver.Remote(command_executor=server, options=options)
# Create a Remote WebDriver instance

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# options=webdriver.EdgeOptions()
# driver=webdriver.edge(options=options)
# Open a website
driver.get("https://www.google.com")

input_element=driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
input_element.send_keys("newageit technologies"+Keys.ENTER)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"newageit"))
)

link=driver.find_element(By.PARTIAL_LINK_TEXT,"newageit")
link.click()

time.sleep(10) 
driver.quit()
