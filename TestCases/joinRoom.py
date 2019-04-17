#coding=utf-8
from airtest.core.api import *
import unittest
import time
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
from othermobile.otherlogin import other_login
class Join(unittest.TestCase):
    dev=ChangeDev()
    devs=dev.changedev()
    u'加入房间'
    @classmethod
    def setUpClass(cls):
        print('加入房间')
    def setUp(self):
        pass
    # @unittest.skip('跳过')
    def test_inputroomNumber(self):
        u'输入房间号'
        getdev = ChangeDev()
        getdev.changedev()
        set_current(0)
        poco = StdPoco()
        time.sleep(1)
        poco("btn_join").click()
        assert(poco("Label_90_0").get_text()=="请输入房间号")
        print('加入房间界面弹出正常，测试通过')
        time.sleep(0.5)
    @unittest.skipIf(hasattr(devs,'get_default_device'),'单设备，跳出此用例执行')
    def test_joinroom(self):
        u'加入房间'
        getdev = ChangeDev()
        getdev.changedev()
        time.sleep(1)
        roomNumber =other_login()
        set_current(0)
        poco = StdPoco()
        for i in range(len(roomNumber)):
            j=roomNumber[i]
            if j:
                poco("btn_code%s"%j).click()
        assert(poco("cancleBtn").get_text()=='退出房间')
        print('加入房间功能测试通过')
    # @unittest.skip('跳过')
    def test_quitroom(self):
        u'退出房间'
        getdev = ChangeDev()
        getdev.changedev()
        set_current(0)
        poco=StdPoco()
        poco("cancleBtn").click()
        poco("btn_yes").click()
        assert(poco("btn_new"))
        print('退出房间功能测试通过')
        set_current(1)
        keyevent('BACK')
        poco = StdPoco()
        poco("btn_yes").click()
        keyevent('BACK')
        poco("btn_yes").click()
        set_current(0)
        poco = StdPoco()
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass