#coding=utf-8
from airtest.core.api import *
from poco.drivers.std import StdPoco
import time,random
id=''.join(str(i) for i in random.sample(range(0,9),6))  #随机生成open ID
from until.ChangeDevs import ChangeDev
def other_login():
    odev=ChangeDev()
    o=odev.changedev()
    set_current(1)
    start_app('com.dashengzhangyou.pykf.lailaiguangdong')
    time.sleep(5)
    poco = StdPoco()
    poco("<Node | Tag = -1").child("Button")[1].click()  #点击进入openid界面
    poco("<Node | Tag = -1").child("<LayerColor | Tag = -1>")[1].child("Widget")[1].click()   #点击openid输入框，方便输入openid
    text(id)  #随机输入5位id
    poco("<Node | Tag = -1").child("<LayerColor | Tag = -1>")[1].child("Button").click()  #点击下方按钮
    time.sleep(3)
    poco("Layout")[1].offspring("city_list").child("root")[0].offspring("btn_1").click()  #选择城市
    poco("Layout")[1].offspring("btn_yes_city").click()   #点击“确定”
    poco("yes").click()  #确认选择城市
    time.sleep(5)
    yzm = poco("lab_regist_verify")
    if yzm.exists():
        poco("closeBtn").click()
    else:
        print('not found')
    poco("btn_new").click()
    poco("btn_select2").child("label_name").click()
    poco("btn_sure").click()
    assert poco("cancleBtn").get_text() == "解散房间"
    roomNumbers=(poco("roomNum").get_text())
    return roomNumbers
