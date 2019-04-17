#coding=utf-8
from poco.drivers.std import StdPoco
from until.openid import openid
import time
poco=StdPoco()
class publicLogin():
    def SelectCity(self):
        poco("Layout")[1].offspring("city_list").child("root")[0].offspring("btn_1").click()
        poco("Layout")[1].offspring("btn_yes_city").click()
        time.sleep(1)
        poco("yes").click()
        closbind=poco("Label_20").wait_for_appearance()
        if classmethod:
            poco("closeBtn").click()