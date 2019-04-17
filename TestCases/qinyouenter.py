#coding=utf-8
from poco.drivers.std import StdPoco
from airtest.core.api import *
from until.ChangeDevs import ChangeDev
import unittest
from BeautifulReport import BeautifulReport
from airtest.core.android import android
from selenium import webdriver
# from until.ScreenShot import ScreenShot
class qinyouentered(unittest.TestCase):
    u'进入亲友圈'
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        enterdev = ChangeDev()
        enterdev.changedev()
        set_current(0)
        # start_app('com.dashengzhangyou.pykf.lailaiguangdong')
        # time.sleep(5)
    @BeautifulReport.add_test_img('test_entered')
    def test_entered(self):
        u'进入亲友圈'
        poco=StdPoco()
        time.sleep(1)
        poco("btn_club").click()
        poco("btn_clubRoom").click()
        assert(poco("Label_39").get_text()=='管理亲友圈房间模版')
        print('进入亲友圈功能--测试通过')
    def tearDown(self):
        # pass
        poco=StdPoco()
        poco("btn_close").click()
        time.sleep(0.5)
        poco("btn_close").click()
    @classmethod
    def tearDownClass(cls):
        pass