#coding=utf-8
from airtest.core.api import *
import unittest
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
from until.Logout import Logouts
from BeautifulReport import BeautifulReport
class Clubqinyou(unittest.TestCase):
    u'亲友俱乐部'
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        u'亲友圈'
        logout=Logouts()
        logout.Logout()
    @BeautifulReport.add_test_img('test_qinyouclub')
    def test_qinyouclub(self):
        u'亲友俱乐部'
        sta=ChangeDev()
        sta.changedev()
        set_current(0)
        start_app('com.dashengzhangyou.pykf.lailaiguangdong')
        time.sleep(6)
        poco=StdPoco()
        poco("<Node | Tag = -1").child("<LayerColor | Tag = -1>")[0].child("Button")[0].click()
        time.sleep(5)
        bind = poco("Label_20")
        if bind.exists():
            poco("closeBtn").click()
        time.sleep(1)
        tip=poco("root").offspring("txt_load")
        time.sleep(15)
        if not tip.exists():
            from until.qinyouhoutai import qinyouhoutai
            callhoutai=qinyouhoutai()
            callhoutai.open_qinyouhoutai()
            poco("btn_club").click()
            assert(poco("Label_60_0").get_text()=='亲友列表')
            print('我的亲友圈界面正常--测试通过')
    def tearDown(self):
        poco = StdPoco()
        poco("btn_close").click()
    @classmethod
    def tearDownClass(cls):
        pass