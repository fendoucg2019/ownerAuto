#coding=utf-8
from until.ChangeDevs import ChangeDev
import unittest
from airtest.core.api import *
from poco.drivers.std import StdPoco
class myreslut(unittest.TestCase):
    u'亲友圈我的战绩界面显示'
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        reslut=ChangeDev()
        reslut.changedev()
        set_current(0)
    def test_myresult(self):
        u'亲友圈我的战绩'
        poco = StdPoco()
        poco("btn_club").click()
        poco("btn_clubRoom").click()
        time.sleep(0.5)
        poco("btn_myRecord").child("Label_42").click()
        assert(poco("btn_search").child("Label_59").get_text() == "搜 索")
        print('亲友圈我的战绩界面显示正常--测试通过')
        poco("btn_sure").click()
    def tearDown(self):
        keyevent("BACK")
        keyevent("BACK")
    @classmethod
    def tearDownClass(cls):
        pass