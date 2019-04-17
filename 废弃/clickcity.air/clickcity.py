# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.std import StdPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# install("D:\\work\\2DAuto\\guangdongmj-V3.apk")
# print('install app')
start_app('com.dashengzhangyou.pykf.lailaiguangdong')
# time.sleep(5)
from poco.drivers.std import StdPoco
poco = StdPoco()

# from airtest.core.api import using
# using('getGdcity.air')
# from getGdCity import Gd
auto_setup(__file__)
print('watting......')
poco("Layout")[1].offspring("city_list").child("root")[0].offspring("btn_1").click()

# poco("<Node | Tag = -1").child("<LayerColor | Tag = -1>")[1].child("Widget")[1].click()
# text('161461')
# text("123")text("dafa")
# text("456456")


# poco("<Node | Tag = -1").child("<LayerColor | Tag = -1>")[1].child("Button").click()
# time.sleep(3)
# Gd.getGDcitylist()
# a=Gd.countGDcity()
# for i in range(a):
#     Gd.clickcity()
#     Gd.removecity()
    # poco("btn_yes_city").click()
    # poco("yes").click()
# poco("<Node | Tag = -1").child("Button")[1]
