#coding=utf-8
from airtest.core.api import *
import unittest,os,sys,io
from until.ChangeDevs import ChangeDev
from poco.drivers.std import StdPoco
class qinyoujoin(unittest.TestCase):
    u'加入亲友房间'
    def setUp(self):
        joinqinyou=ChangeDev()
        joinqinyou.changedev()
        set_current(0)
    def test_joinqinyou(self):
        u'测试加入亲友房间'
        poco=StdPoco()
        poco("btn_club").click()
        poco("btn_clubRoom").click()
        if poco("btn_enterRoom").child("Label_39").exists():
            poco("btn_enterRoom").child("Label_39").click()
            assert(poco("cancleBtn").get_text() == '退出房间')
            print('加入自己创建的房间--测试通过')
            poco("cancleBtn").click()
            poco("btn_yes").click()
        else:
            u'测试失败'
            print('not found')
    def tearDown(self):
        pass