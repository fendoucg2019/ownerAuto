#coding=utf-8
from airtest.core.api import *
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
import unittest
class qinyou_xianliao(unittest.TestCase):
    u'测试调闲聊应用'
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        xianliao=ChangeDev()
        xianliao.changedev()
        set_current(0)
    def test_callxianliao(self):
        u'测试亲友圈通过闲聊邀请好友'
        poco=StdPoco()
        poco("btn_club").click()
        poco("btn_clubRoom").click()
        time.sleep(0.5)
        poco("btn_clubInfo").child("Label_42").click()
        poco("Image_16").click()
        poco("btn_xianliao2").click()
        assert (poco("root").offspring("txt").get_text() == '提示：闲聊分享失败，未检测到闲聊App')
        print('调用闲聊功能--测试通过')
        time.sleep(1)
    def tearDown(self):
        keyevent("BACK")
        keyevent("BACK")
        keyevent("BACK")
    @classmethod
    def tearDownClass(cls):
        pass