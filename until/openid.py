#coding=utf-8
import random
from airtest.core.api import *
id=''.join(str(i) for i in random.sample(range(0,9),6))  #随机生成open ID
from poco.drivers.std import StdPoco
poco = StdPoco()
class openid():
    def input_id(self):
        u'输入ID'
        if poco("<Node | Tag = -1").child("Button")[1]:
            poco("<Node | Tag = -1").child("Button")[1].click()
            poco("<Node | Tag = -1").child("<LayerColor | Tag = -1>")[1].child("Widget")[1].click()
            text(id)
            poco("<Node | Tag = -1").child("<LayerColor | Tag = -1>")[1].child("Button").click()
            time.sleep(2)
