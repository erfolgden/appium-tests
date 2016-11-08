import unittest

from appium import webdriver

class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['testobject_api_key'] = '45EA9BDA6AD3471785987A32A53450B4'
        desired_caps['testobject_app_id'] = '1'
        desired_caps['testobject_device'] = 'iPhone_5_16GB_real'

        self.driver = webdriver.Remote('http://appium.testobject.com/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_get_settings(self):
        settings = self.driver.get_settings()
        self.assertIsNotNone(settings)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)