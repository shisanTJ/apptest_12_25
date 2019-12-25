from base.base import Base
from page.page_ele import PageEle


class PageNew(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    def click_new_msg(self):
        self.click_ele(PageEle.new_msg)
