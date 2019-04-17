#coding=utf-8
from airtest.core.api import *
import time
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
import unittest
class createqinyourooms(unittest.TestCase):
    u'创建亲友房'
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        u'测试创建亲友房'
        qinyouroom=ChangeDev()
        qinyouroom.changedev()
        set_current(0)
    def test_createqyroom(self):
        u'创建亲友房间'
        poco = StdPoco()
        poco("btn_club").click()
        poco("btn_clubRoom").click()
        time.sleep(0.5)
        zhuanshi=poco("lab_diamondState").get_text()
        if zhuanshi=='可用':
            poco("btn_invite").child("Label_42").click()
            poco("Layout")[8].offspring("list_view_select").offspring("label_name")[1].click()
            poco("Layout")[14].offspring("btn_sure").click()
            time.sleep(0.5)
            assert(poco("cancleBtn").get_text()=="解散房间")
            print('创建亲友房功能--测试通过')
        else:
            assert(poco("lab_diamondState").get_text()=='可用')
            print('没有钻石可用，创建亲友房间功能--测试失败')
            poco("btn_close").click()
            time.sleep(0.5)
            poco("btn_close").click()

    def test_jiesanqyroom(self):
        u'解散亲友房'
        poco=StdPoco()
        poco("cancleBtn").click()
        poco("btn_yes").click()
        assert(poco("Label_39").get_text()=='管理亲友圈房间模版')
        print('解散亲友房--测试通过')
    # def test_joinroom(self):
    #     u'创建亲友圈房间后，自己加入创建的房间'
    #     poco = StdPoco()
    #     poco("Label_39").click()
    #     assert(poco("cancleBtn").get_text()=='退出房间')
    #     print('加入自己创建的房间--测试通过')
    #     poco("cancleBtn").click()
    #     poco("btn_yes").click()
    def tearDown(self):
        keyevent('BACK')
        keyevent('BACK')
    @classmethod
    def tearDownClass(cls):
        pass