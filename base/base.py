

from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver =driver
    # 定位元素
    def find_ele(self,loc,timeout=5,poll_frequency=1):
       return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(loc[0],loc[1]))
    # 定位多个元素
    def find_eles(self,loc,timeout=5,poll_frequency=1):
       return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(loc[0],loc[1]))
    # 点击单个元素
    def click_ele(self,loc,timeout=5,pull_frequency=1):
        self.find_ele(loc,timeout,pull_frequency).click()
    # 定位输入框
    def input_ele(self,loc,text,timeout=5,pull_frequency=1):
        self.find_ele(loc,timeout,pull_frequency).clear()
        self.find_ele(loc,timeout,pull_frequency).send_keys(text)