import pytest,sys,os


from base.page import Page

sys.path.append(os.getcwd())
from base.get_driver import get_driver
@pytest.fixture(params=['hello','python','appium'])
def data(request):
    return request.param


class TestSendMsg():
    def setup_class(self):
        self.driver =get_driver("com.android.mms",".ui.ConversationList")

        self.page =Page(self.driver)
    def teardown_class(self):
        self.driver.quit()
    # 点击新建信息输入收件人
    @pytest.fixture(scope="class",autouse=True)
    def click_msg(self,tel=15731321747):
        self.page.click_new_msg_bot().click_new_msg()
        # 收件人
        self.page.input_send_name_bot().input_send_name(tel)

    def test01_msg(self,data):

        # 发送信息
        self.page.input_send_text_bot().send_msg_bot(data)
        # 点击发送

        print("发送成功")
