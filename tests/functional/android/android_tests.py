import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from appium import webdriver
from dateutil.parser import parse

from tests.apps.config import TEST_OBJECT_API_KEY, TEST_OBJECT_APP_ID


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['testobject_api_key'] = TEST_OBJECT_API_KEY
        desired_caps['testobject_app_id'] = TEST_OBJECT_APP_ID
        desired_caps['testobject_device'] = 'LG_Nexus_5X_real'

        self.driver = webdriver.Remote('http://appium.testobject.com/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_get_settings(self):
        settings = self.driver.get_settings()
        self.assertIsNotNone(settings)

    def test_simple_actions(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, 'CONFIG')),
                        message="Unable to find element")
        el = self.driver.find_element_by_name('CONFIG')
        el.click()
        assert self.driver.find_element_by_name('Config').is_displayed()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)