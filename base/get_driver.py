
from appium import webdriver


def get_driver(apc, act):
    """移动端自动化基本代码"""
    # 导包

    # 创建驱动对象
    import time



    capabilities = {"platformName": "Android",
                    "platformVersion": "5.1",
                    "deviceName": "SAMSUNG Galasy s6",
                    "appPackage": apc,
                    "appActivity": act,
                    "resetKeyboard": True,
                    "unicodeKeyboard": True
                    }

    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=capabilities)
