#coding=utf-8
from airtest.core.api import *
import unittest
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
class creatgd(unittest.TestCase):
    u'广东服/创建房间'
    @classmethod
    def setUpClass(cls):
        print('运行创建房间用例')
    def setUp(self):
        getdev = ChangeDev()
        getdev.changedev()
        print('创建房间模块用例')
    def test_creatrooms(self):
        u'创建房间'
        getdev = ChangeDev()
        getdev.changedev()
        set_current(0)
        poco = StdPoco()
        if poco("img_yuanbao").exists():
            poco("closeBtn").click()
            if poco("btn_new").exists():
                poco("btn_new").click()
                if poco("pan_newer_ddz").exists():
                    poco("Layout")[6].offspring("Image_bg").click()
                    poco("Layout")[6].offspring("list_view_select").offspring("btn_select1").click()
                    poco("Layout")[7].offspring("btn_sure").click()
                    assert(poco("cancleBtn").get_text() == "解散房间")
                    print('测试通过')
                else:
                    poco("btn_select2").child("label_name").click()
                    poco("btn_sure").click()
                    assert(poco("cancleBtn").get_text() == "解散房间")
                    print('测试通过')
            else:
                assert_equal(1,2,msg='没找元素，测试失败')
        else:
            if poco("btn_new").exists():
                poco("btn_new").click()
                poco("btn_select2").child("label_name").click()
                poco("btn_sure").click()
                assert (poco("cancleBtn").get_text() == "解散房间")
                print('测试通过')

    # @unittest.skip('跳过')
    def test_dismissroom_Cancel(self):
        u'取消解散房间'
        poco = StdPoco()
        poco("cancleBtn").click()
        dismiss_cancel = poco("<Label | Tag = -1, Label = '您是否要解散房间?'>")
        dismiss_cancel.wait_for_appearance()
        poco("btn_cancal").click()
        assert(poco("shardBtn").get_text()=='邀请好友')
        print('测试通过')
    # @unittest.skip('跳过')
    def test_dismissroom_Sure(self):
        u'解散房间'
        poco = StdPoco()
        poco("cancleBtn").click()
        dismiss = poco("<Label | Tag = -1, Label = '您是否要解散房间?'>")
        dismiss.wait_for_appearance()
        poco("btn_yes").click()
        time.sleep(5)
        assert(poco("btn_join"))
        print('测试通过')
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass