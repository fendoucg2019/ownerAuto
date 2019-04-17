#coding=utf-8
from airtest.core.api import *
from poco.drivers.std import StdPoco
import unittest
from until.ChangeDevs import ChangeDev
class gz(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        gzDev=ChangeDev()
        gzDev.changedev()
        set_current(0)
   # @unittest.skip('skip')
    def test_gz(self):
        '规则界面跳转测试'
        poco=StdPoco()
        poco("btn_more").click()
        poco("btn_ruler").click()
        if poco("Label_9_0"):
            print('规则界面弹出正常--测试通过')
        else:
            print('规则界面弹出异常--测试失败')
            assert (poco("Label_9_0"))
        poco("clost_button").click()
        poco("btn_close_morepanel2").click()
    def test_gzmore(self):
        '规则界面更多按钮跳转测试'
        poco=StdPoco()
        poco("btn_more").click()
        poco("btn_ruler").click()
        poco("Button_drop").click()
        poco("list_view_select").offspring("btn_select2").child("label_name").click()
        if poco("list_view_select").offspring("btn_select2").child("label_name"):
            print('更多按钮及选择玩法后规则展示正常--测试通过')
        else:
            print('更多按钮跳转异常--测试失败')
            assert(poco("list_view_select").offspring("btn_select2").child("label_name"))
        poco("clost_button").click()
        poco("btn_close_morepanel2").click()
        def tearDown(self):
            pass
        @classmethod
        def tearDownClass(cls):
            pass