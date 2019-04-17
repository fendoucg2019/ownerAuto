#coding=utf-8
from until.ChangeDevs import ChangeDev
import time
from airtest.core.api import *
import unittest
from poco.drivers.std import StdPoco
class getDiamond(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        getDiamondDev=ChangeDev()
        getDiamondDev.changedev()
        set_current(0)
    def test_getDiamond(self):
        '钻石界面跳转测试'
        poco=StdPoco()
        poco("btn_yaoqing").click()
        assert (poco("Label_75").get_text() == '分享后得钻石(好友注册无法再获奖励)')
        print('领取钻石界面显示正常--测试通过')
    def test_getklq(self):
        '可领取界面跳转测试'
        poco=StdPoco()
        poco("btn_pan2").child("Image_unselect").child("lab_pan1").click()
        assert(poco("lab_bg1").get_text()=='当前可领取:')
        print('可领取界面显示正常--测试通过')
        poco("Image_26").click()
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass