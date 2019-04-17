#coding=utf-8
import unittest
from airtest.core.api import *
from until.ChangeDevs import ChangeDev
from poco.drivers.std import StdPoco
class qinyoulists(unittest.TestCase):
    u'进入亲友列表'
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        qinyougetdev=ChangeDev()
        qinyougetdev.changedev()
        set_current(0)
    def test_qinyoulist(self):
        u'亲友列表'
        poco=StdPoco()
        poco("btn_club").click()
        if poco("btn_clublist").exists():
            poco("btn_clublist").click()
            assert(poco("lab_title").get_text()=='亲友圈玩家')
            print('亲友圈玩家界面展示正常--测试通过')
    def tearDown(self):
        poco=StdPoco()
        poco("btn_close").click()
        poco("btn_close").click()
    @classmethod
    def tearDownClass(cls):
        pass