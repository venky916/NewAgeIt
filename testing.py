import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        service=Service(executable_path="chromedriver.exe")
        self.driver=webdriver.Chrome(service=service)

    def test_search_in_pythonOrg(self):
        driver=self.driver
        driver.get("https://www.python.org/")
        print('hello'+driver.title)

        # assertion to confirm if title has python keyword in it
        self.assertIn("Python", driver.title)
        elem=driver.find_element(By.NAME,"q")
 
        # send data
        elem.send_keys("pycon")

        # receive data
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
 
    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()


