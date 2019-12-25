from page.page_new import PageNew
from page.page_send_msg import PageSendMsg

class Page():
    def __init__(self,driver):
        self.driver =driver
    def click_new_msg_bot(self):
        return PageNew(self.driver)

    def input_send_name_bot(self):
        return PageSendMsg(self.driver)

    def input_send_text_bot(self):
        return  PageSendMsg(self.driver)

