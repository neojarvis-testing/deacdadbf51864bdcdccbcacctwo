# import pytest
from base import BaseTest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

class Test_Page(BaseTest):

    def setUp(self):
        url = "https://www.mumzworld.com/en"
        self.driver = self.setUpDriver()
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_method_name(self):
    

        print(sys.executable)

 
