from selenium.webdriver.common.by import By


class PageEle():
# 点击新建信息com.android.mms:id/action_compose_new   全是ID
# 收件人com.android.mms:id/recipients_editor
# 发送的信息com.android.mms:id/embedded_text_editor
# 发送按钮com.android.mms:id/send_button_sms
#     信息类
#    新建信息
    new_msg=(By.ID,"com.android.mms:id/action_compose_new")
    # 收件人
    send_name =(By.ID,"com.android.mms:id/recipients_editor")
    # 编写发送信息
    send_msg=(By.ID,"com.android.mms:id/embedded_text_editor")
    # 发送按钮
    send_button =(By.ID,"com.android.mms:id/send_button_sms")
