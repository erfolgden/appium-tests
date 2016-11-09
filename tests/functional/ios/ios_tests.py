import unittest

import time
from appium import webdriver

from tests.apps.config import TEST_OBJECT_API_KEY, TEST_OBJECT_APP_ID


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['testobject_api_key'] = TEST_OBJECT_API_KEY
        desired_caps['testobject_app_id'] = TEST_OBJECT_APP_ID
        desired_caps['testobject_device'] = 'iPhone_5_16GB_real'

        self.driver = webdriver.Remote('http://appium.testobject.com/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_get_settings(self):
        settings = self.driver.get_settings()
        self.assertIsNotNone(settings)

    def test_simple_actions(self):
        time.sleep(2)
        el = self.driver.find_element_by_accessibility_id('Graphics')
        el.click()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)