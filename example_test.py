import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchText(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.google.com/")
        time.sleep(3)
        afwijzen = self.driver.find_elements(By.TAG_NAME, "button")[2]
        afwijzen.click()

    def test_search_by_text(self):
        return

    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()
