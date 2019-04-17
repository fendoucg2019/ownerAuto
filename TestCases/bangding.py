#coding=utf-8
from airtest.core.api import *
from until.ChangeDevs import ChangeDev
import unittest
from poco.drivers.std import StdPoco
class bingdingshouji(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        bdDev=ChangeDev()
        bdDev.changedev()
        set_current(0)
    def test_bd(self):
        '首页绑定跳转测试'
        poco=StdPoco()
        poco("btn_bind_phone").click()
        if poco("phone_title"):
            print('绑定跳转功能--测试通过')
        else:
            print('绑定跳转功能--测试失败')
            assert (poco("phone_title"))
    def tearDown(self):
        keyevent("BACK")
    @classmethod
    def tearDownClass(cls):
        pass
