#coding=utf-8
from until.ChangeDevs import ChangeDev
import unittest
from poco.drivers.std import StdPoco
from airtest.core.api import *
class mianfeia(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        mainfeiDev=ChangeDev()
        mainfeiDev.changedev()
        set_current(0)
    def test_mianfei(self):
        '首页免费按钮跳转测试'
        poco=StdPoco()
        poco("btn_free").click()
        if poco("lb_des"):
            print('首页免费跳转功能正常--测试通过')
        else:
            print('首页免费跳转功能异常--测试失败')
            assert (poco("lb_des_0").get_text() == '每日限领一次(二选一)')
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        keyevent("BACK")