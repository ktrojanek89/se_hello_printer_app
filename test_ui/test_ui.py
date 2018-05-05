from selenium import webdriver
import unittest
import time


# mkdir -p test_ui
# atom test_ui/test_ui.py
#
# https://github.com/wojciech11/se_intro_selenium
#

@pytest.mark.webtestst
class TestFormater(unittest.TestCase):
    def test_plain_lowercase(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000/ui")
        time.sleep(1000)
