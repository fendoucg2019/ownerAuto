#coding=utf-8
from airtest.core.api import *
from poco.drivers.std import StdPoco
import  unittest
from until.ChangeDevs import ChangeDev
class morebutton(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        moreDev=ChangeDev()
        moreDev.changedev()
        set_current(0)
    def test_moreButton(self):
        '更多按钮弹出测试'
        poco=StdPoco()
        poco("btn_more").click()
        if poco("Label_back"):
            print('更多按钮弹出功能正常--测试通过')
        else:
            print('更多按钮弹出失败--测试失败')
            assert(poco("Label_back").get_text()=='账号设置')
        poco("btn_close_morepanel2").click()
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass