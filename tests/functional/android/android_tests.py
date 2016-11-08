import unittest

from appium import webdriver
from dateutil.parser import parse


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['testobject_api_key'] = '7B904715A6A04BA5BA0A1213CF39C77B'
        desired_caps['testobject_app_id'] = '1'
        desired_caps['testobject_device'] = 'LG_Nexus_5X_real'

        self.driver = webdriver.Remote('http://appium.testobject.com/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_get_settings(self):
        settings = self.driver.get_settings()
        self.assertIsNotNone(settings)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)