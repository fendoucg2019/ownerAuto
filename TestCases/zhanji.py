#coding=utf-8
from airtest.core.api import *
import unittest
import time
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
class zhanjibrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        zhanjiDev=ChangeDev()
        zhanjiDev.changedev()
        set_current(0)
    def test_zhanjishow(self):
        '首页战绩测试'
        poco=StdPoco()
        poco("btn_record").click()
        recode = poco("lab_title").get_text()
        if recode == '战绩记录':
            print("\033[31;0m战绩记录界面显示正常--测试通过\033[0m")
        else:
            print("\033[1;41m战绩记录界面显示异常--测试失败\033[0m")
            assert(poco("lab_title").get_text()=='战绩记录')
        poco("close_btn").click()
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass