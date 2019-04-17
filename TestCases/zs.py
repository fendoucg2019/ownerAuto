#coding=utf-8
from until.ChangeDevs import ChangeDev
import unittest
from poco.exceptions import PocoTargetTimeout
from poco.drivers.std import StdPoco
from airtest.core.api import *
class zuanshichongzhi(unittest.TestCase):
    '钻石充值功能'
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        chongzhi=ChangeDev()
        chongzhi.changedev()
        set_current(0)
    def test_zs(self):
        '跳转商城测试'
        poco=StdPoco()
        poco("btn_diamond_add").click()
        try:
            poco(("Label_5_shadow"), type='Text').wait_for_appearance(5)
            print('跳转钻石商城--测试通过')
        except PocoTargetTimeout:
            print('跳转钻石商城--测试失败')
            raise
    def test_zsx6(self):
        '钻石x6充值测试跳转'
        poco=StdPoco()
        poco("Layout")[1].offspring("listview").child("root")[0].offspring("btn_buy").click()
        if poco("title").exists():
            print('充值跳转正常--测试通过')
        else:
            print('充值界面跳转异常--测试失败')
            assert(poco("title"))
    def test_zsx6zfb(self):
        '支付宝充钻石x6跳转测试'
        poco=StdPoco()
        poco("Layout")[1].offspring("listview").child("root")[0].offspring("btn_buy").click()
        poco("btn_zfb").click()
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        if poco("com.eg.android.AlipayGphone:id/normal_reg_highlight_layout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[0].offspring("android.widget.EditText").exists():
            keyevent("BACK")
            print('支付宝充值跳转--测试通过')
        else:
            print('支付宝充值跳转--测试失败')
            assert(poco("com.eg.android.AlipayGphone:id/normal_reg_highlight_layout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[0].offspring("android.widget.EditText"))
    def test_zsx6weixin(self):
        '微信充钻石x6跳转测试'
        poco=StdPoco()
        poco("Layout")[1].offspring("listview").child("root")[0].offspring("btn_buy").click()
        poco("btn_wx").click()
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        if poco("android.widget.FrameLayout").offspring("android:id/text1").exists():
            print('微信充值跳转--测试通过')
            poco("android.widget.FrameLayout").offspring("com.tencent.mm:id/kb").click()
        else:
            print('微信充值跳转--测试失败')
            assert(poco("android.widget.FrameLayout").offspring("android:id/text1"))
    def test_zsx15(self):
        '钻石x15充值测试跳转'
        poco=StdPoco()
        poco("Layout")[1].offspring("listview").child("root")[1].offspring("btn_buy").click()
        if poco("title").exists():
            print('充值跳转正常--测试通过')
        else:
            print('充值界面跳转异常--测试失败')
            assert(poco("title"))
    def test_zsx15zfb(self):
        '支付宝充钻石x15跳转测试'
        poco=StdPoco()
        poco("Layout")[1].offspring("listview").child("root")[1].offspring("btn_buy").click()
        poco("btn_zfb").click()
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        if poco("com.eg.android.AlipayGphone:id/normal_reg_highlight_layout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[0].offspring("android.widget.EditText").exists():
            keyevent("BACK")
            print('支付宝充值跳转--测试通过')
        else:
            print('支付宝充值跳转--测试失败')
            assert(poco("com.eg.android.AlipayGphone:id/normal_reg_highlight_layout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[0].offspring("android.widget.EditText"))
    def test_zsx15weixin(self):
        '微信充钻石x15跳转测试'
        poco=StdPoco()
        poco("Layout")[1].offspring("listview").child("root")[1].offspring("btn_buy").click()
        poco("btn_wx").click()
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        if poco("android.widget.FrameLayout").offspring("android:id/text1").exists():
            print('微信充值跳转--测试通过')
            poco("android.widget.FrameLayout").offspring("com.tencent.mm:id/kb").click()
        else:
            print('微信充值跳转--测试失败')
            assert(poco("android.widget.FrameLayout").offspring("android:id/text1"))
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        keyevent('BACK')