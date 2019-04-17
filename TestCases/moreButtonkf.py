#coding=utf-8
from airtest.core.api import *
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
import unittest

class kefu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        kefDev=ChangeDev()
        kefDev.changedev()
        set_current(0)
    # @unittest.skip('skip')
    def test_kf(self):
        '客服跳转功能测试'
        poco=StdPoco()
        poco("btn_more").click()
        poco("btn_help").click()
        if poco("Layout")[1].offspring("Label_8"):
            print('客服界面跳转正常--测试通过')
        else:
            print('客服界面跳转异常--测试失败')
            assert(poco("Layout")[1].offspring("Label_8"))
    def test_kfonline(self):
        '跳转到在线客服测试'
        poco=StdPoco()
        poco("Layout")[1].offspring("btn_kefu").click()
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        if poco("com.dashengzhangyou.pykf.lailaiguangdong:id/message_fragment_container").offspring("com.dashengzhangyou.pykf.lailaiguangdong:id/messageListView").child("android.widget.RelativeLayout")[0].offspring("com.dashengzhangyou.pykf.lailaiguangdong:id/message_item_content").offspring("com.dashengzhangyou.pykf.lailaiguangdong:id/clickable_item_text"):
            self.rgkf=poco("com.dashengzhangyou.pykf.lailaiguangdong:id/message_fragment_container").offspring("com.dashengzhangyou.pykf.lailaiguangdong:id/messageListView").child("android.widget.RelativeLayout")[0].offspring("com.dashengzhangyou.pykf.lailaiguangdong:id/message_item_content").offspring("com.dashengzhangyou.pykf.lailaiguangdong:id/clickable_item_text")
            if self.rgkf.get_text()=='人工客服':
                print('客服系统跳转--测试通过')
                keyevent("BACK")
        else:
            print('客服系统跳转异常--测试失败')
            assert(self.rgkf.get_text()=='人工客服')
    def test_kfwxcopy(self):
        '复制微信公众号'
        poco=StdPoco()
        # poco("Layout")[1].offspring("ItemList").child("root")[0].offspring("Button_copy").click()
        touch((916, 266), duration=0.1)
        if poco("root").offspring("txt"):
            if poco("root").offspring("txt").get_text()=='复制信息成功':
                print('复制微信公众号--测试通过')
        else:
            print('复制微信公众号异常--测试失败')
            assert(poco("root").offspring("txt"))
    def test_kfdlcopy(self):
        '复制代理微信'
        poco=StdPoco()
        touch((922,450),duration=0.1)
        if poco("root").offspring("txt"):
            if poco("root").offspring("txt").get_text()=='复制信息成功':
                print('复制代理招募--测试通过')
        else:
            print('复制代理招募异常--测试失败')
            assert(poco("root").offspring("txt"))

    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        poco=StdPoco()
        keyevent('BACK')
        poco("btn_close_morepanel2").click()

