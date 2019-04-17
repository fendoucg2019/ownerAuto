#coding=utf-8
from until.ChangeDevs import ChangeDev
import unittest
from airtest.core.api import *
import time
from poco.drivers.std import StdPoco
class redpackets(unittest.TestCase):
    u'红包兑换'
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        redpak=ChangeDev()
        redpak.changedev()
        set_current(0)
    def test_aredpacket(self):
        u'兑换奖品界面展示'
        poco=StdPoco()
        # start_app('com.dashengzhangyou.pykf.lailaiguangdong')
        # time.sleep(5)
        redbox=poco("pan_bottom").child("btn_exchange")
        if redbox.exists():
            redbox.click()
        dhjp=poco("Layout")[1].offspring("btn_trophy").offspring("lab") #兑换奖品
        if dhjp.exists():
           print('兑换奖品界面显示--测试通过')
        else:
            print('测试失败')
            assert(poco("Layout")[1].offspring("btn_trophy").offspring("lab"))
    def test_huafeiexChange(self):
        u'元宝兑话费功能测试'
        poco=StdPoco()
        poco("Layout")[1].offspring("itemList").offspring("panel").child("btn_get").click()  #点击 红包兑换 按钮
        yuanbao=int(poco("Layout")[1].offspring("lab_scrip").get_text()) #将获取到的元宝转为整形
        x1000 = poco("Layout")[1].offspring("itemList").offspring("lab_num").get_text() #获取按钮中文本
        x2000=poco("Layout")[1].offspring("itemList").child("root")[1].offspring("lab_num").get_text()
        x3000=poco("Layout")[1].offspring("itemList").child("root")[2].offspring("lab_num").get_text()
        j1000=int(x1000.split('x')[1]) #获取文本的额度并将转为整形
        j2000 = int(x2000.split('x')[1])
        j3000=int(x3000.split('x')[1])
        if yuanbao<j1000:  #判断元宝与额度的匹配
            touch((890, 540), duration=0.1)
            tip = poco("root").offspring("txt")  # 元宝不足提示
            if tip.get_text()=='元宝不足，无法兑换':
                print('现有元宝小于限制元宝，无法进行话费兑换，测试通过')
            else:
                print('现有元宝小于限制元宝，能兑换话费，测试失败')
                assert(poco("root").offspring("txt"))
        elif j1000<yuanbao<j2000:
            touch((890, 540), duration=0.1)
            x1000tip=poco("txt_content").get_text()
            if x1000tip=='是否确认消耗1000个元宝兑换随机1元~3元话费':
                print('弹出1000元宝兑换界面正常--测试通过')
                poco("btn_yes").click()
                time.sleep(3)
                bdmobile=poco("phone_login_title").get_text()
                if bdmobile=='绑定手机号':
                    print('1000元宝兑换功能--测试通过')
            else:
                print('1000元宝兑换功能--测试失败')
                assert(poco("txt_content").get_text()=='是否确认消耗1000个元宝兑换随机1元~3元话费')
        keyevent('BACK')
    def test_dhrecode(self):
        u'兑换记录 界面显示'
        poco=StdPoco()
        poco("lab").click()
        time.sleep(1)
        assert(poco("Layout")[1].offspring("btn_record").offspring("lab").get_text()=='兑换记录')
        print('兑换记录界面显示正常--测试通过')
        poco("Layout")[1].offspring("btn_trophy").offspring("lab").click()
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
        keyevent("BACK")