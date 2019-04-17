#coding=utf-8
from airtest.core.api import *
from poco.drivers.std import StdPoco
import unittest
from until.ChangeDevs import ChangeDev
class notices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        notDev=ChangeDev()
        notDev.changedev()
        set_current(0)
    def test_notice(self):
        '消息测试'
        poco=StdPoco()
        poco("btn_more").click()
        poco("btn_mail").click()
        if poco("Layout")[1].offspring("Panel_bg").child("lab_title").exists():
            print('消息界面跳转成功--测试通过')
        else:
            print('消息界面跳转异常--测试失败')
            assert (poco("Layout")[1].offspring("Panel_bg").child("lab_title").get_text == '消息')
        poco("Layout")[1].offspring("Image_78").click()
        poco("btn_close_morepanel2").click()
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass