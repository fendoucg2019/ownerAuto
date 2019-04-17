#coding=utf-8
from airtest.core.api import *
import unittest
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
class Shares(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        sharDev=ChangeDev()
        sharDev.changedev()
        set_current(0)
    def test_share(self):
        '首页分享界面弹出功能测试'
        poco=StdPoco()
        poco("btn_share").click()
        if poco("friend_group_btn").exists():
            print('分享界面弹出成功')
        else:
            print('分享界面弹出失败')
            assert (poco("friend_group_btn"))
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        keyevent('BACK')