#coding=utf-8
from airtest.core.api import *
from poco.drivers.std import StdPoco
import unittest
from until.ChangeDevs import ChangeDev
class moreButto_zh(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        zhDev=ChangeDev()
        zhDev.changedev()
        set_current(0)
    def test_zh(self):
        '账号设置测试'
        poco=StdPoco()
        poco("btn_more").click()
        poco("Label_back").click()
        if poco("btn_account"):
            print('账号设置跳转正常--测试通过')
        else:
            print('账号设置跳转异常--测试失败')
            assert (poco("btn_account"))
        keyevent('BACK')
        poco("btn_close_morepanel2").click()
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass