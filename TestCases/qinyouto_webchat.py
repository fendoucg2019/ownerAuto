#coding=utf-8
from until.ChangeDevs import ChangeDev
import unittest
from airtest.core.api import *
from poco.drivers.std import StdPoco
class qinyouinfos(unittest.TestCase):
    u'亲友圈我的战绩界面显示'
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        qinyouinfo=ChangeDev()
        qinyouinfo.changedev()
        set_current(0)
    def test_webchatinvait(self):
        u'微信邀请'
        poco = StdPoco()
        poco("btn_club").click()
        poco("btn_clubRoom").click()
        time.sleep(0.5)
        poco("btn_clubInfo").child("Label_42").click()
        poco("Image_16").click()
        assert (poco("lab_str").get_text() == '亲友圈ID已复制，请前往微信或闲聊分享')
        print('邀请好友按钮弹窗显示正常，有“前往微信/前往闲聊接口”')
        poco("btn_wechat2").click()
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        assert (poco("android:id/text1").get_text() == '登录微信')
        print('通过微信邀请好友调用微信正常--测试通过')
        poco("android.widget.FrameLayout").offspring("com.tencent.mm:id/kb").click()

    def tearDown(self):
        keyevent('BACK')
        keyevent('BACK')
        keyevent('BACK')
    @classmethod
    def tearDownClass(cls):
        pass
