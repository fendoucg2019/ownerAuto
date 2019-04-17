#coding=utf-8
from airtest.core.api import *
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
import unittest
from base64 import b64decode
from BeautifulReport import BeautifulReport
class entersetting(unittest.TestCase):
    '系统设置测试'
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        setDev=ChangeDev()
        setDev.changedev()
        set_current(0)
    # @BeautifulReport.stop
    def test_set(self):
        '设置界面跳转测试'
        poco=StdPoco()
        poco("btn_more").click()
        poco("btn_setting").click()
        if poco("zhendong").exists():
            print('进入设置界面--测试通过')
        else:
            print('进入设置界面异常--测试失败')
            assert(poco("zhendong").get_text()=='震动')
    def test_setselecwjsound(self):
        '屏蔽玩家声音测试'
        poco=StdPoco()
        pb=poco("select_CheckBox")
        if pb.attr('enabled')==True:
            pb.click()
            print('屏蔽玩家语音选择正常--测试通过')
        else:
            print('无法勾选“屏蔽玩家语音”--测试失败')
            assert(pb.attr('enabled')==True)
    @unittest.skip('跳过')
    def test_setyinxiao(self):
        '音效设置测试'
        poco=StdPoco()
        #实现截图并对比
        b64, fmt = poco.snapshot(width=720)
        i=str(1)
        j=str(2)
        savescreen = open('D:\\work\\abc\\{}.png'.format(i), 'wb').write(b64decode(b64))
        poco("sound_on_off").click()
        b65, fmt1 = poco.snapshot(width=720)
        savescreen1= open('D:\\work\\abc\\{}.png'.format(j), 'wb').write(b64decode(b64))
        if savescreen!=savescreen1:
            print('设置音乐功能--测试通过')
        else:
            print('设置音乐功能--测试失败')
            assert(savescreen==savescreen1)
        keyevent("BACK")
        poco("btn_close_morepanel2").click()
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass