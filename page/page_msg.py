from base.base import Base
from page.page_ele import PageEle


class PageMsg(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    # 点击新建信息
    def click_new_msg(self):
        self.click_ele(PageEle.new_msg)
    # 输入收件人
    def input_send_name(self,text):
        self.input_ele(PageEle.send_name,text)
    # 编辑信息
    def input_send_msg(self,text):
        self.input_ele(PageEle.send_msg,text)
    # 点击发送信息
    def click_send_msg(self):
        self.click_ele(PageEle.send_button)