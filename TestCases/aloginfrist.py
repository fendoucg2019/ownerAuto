#coding=utf-8
from airtest.core.api import *
import unittest
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
from BeautifulReport import BeautifulReport

class loginfirst(unittest.TestCase):
    u'登录相关用例'
    @classmethod
    def setUpClass(cls):
        print('初始化')
    def setUp(self):
        print('登录模块用例')
        getdev=ChangeDev()
        getdev.changedev()
    def test_loginfirst(self):
        u'测试登录'
        set_current(0)
        start_app('com.dashengzhangyou.pykf.lailaiguangdong')
        time.sleep(20)
        poco = StdPoco()
        from until.openid import openid
        id=openid()
        id.input_id()
        self.assertTrue(poco("lab_title").get_text() == "选择地区")
        print('测试通过')
    def test_selectcity(self):
        u'选择城市'
        poco = StdPoco()
        poco("Layout")[1].offspring("city_list").child("root")[0].offspring("btn_1").click()
        poco("Layout")[1].offspring("btn_yes_city").click()
        time.sleep(1)
        poco("yes").click()
        assert(poco("bind_pho_num").get_text() == "手机号：")
        print('测试通过')
        poco("closeBtn").click()
    @unittest.skip('暂时跳过')
    def binddmobile(self):
        u'绑定手机'
        from until.yanzhengma import yzm
        poco=StdPoco()
        poco("input_phone").click()
        text('13711111111')
        poco("btn_getverify").click()
        poco("input_verify_pho").click()
        inputyzm = yzm()
        text(inputyzm)
        poco("btn_sure").click()
        poco("input_newpw").click()
        text('123456')
        poco("input_newpw2").click()
        text('123456')
        poco("btn_setpw_sure").click()
        SureBind=poco("Label_302")
        SureBind.wait_for_appearance()
        assert SureBind.get_text()=='您将绑定的手机号为：'
        poco("btn_sure2").click()

    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass