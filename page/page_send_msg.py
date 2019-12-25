from base.base import Base
from page.page_ele import PageEle

class PageSendMsg(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def input_send_name(self,tel):
        self.input_ele(PageEle.send_name,tel)

    def send_msg_bot(self,text):
        self.input_ele(PageEle.send_msg,text)
        self.click_ele(PageEle.send_button)