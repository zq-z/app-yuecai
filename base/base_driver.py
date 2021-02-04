from appium import webdriver


class Base_driver:
    def __init__(self):
        desired_caps = dict()
        '''安卓信息'''
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = "7.1.2"
        desired_caps['deviceName'] = '127.0.0.1:62001'
        '''app信息'''
        desired_caps['appPackage'] = 'com.wosen8.yuecai'
        desired_caps['appActivity'] = '.ui.activity.SplashActivity'
        '''输入中文'''
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver= webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        return self.driver

