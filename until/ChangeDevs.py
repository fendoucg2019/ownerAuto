#encoding=utf-8
from airtest.core.api import *
from airtest.core.android.adb import ADB
class ChangeDev():
    def changedev(self):
        adb=ADB()
        devs=adb.devices()
        if len(devs)==1:
            devs1 = devs[0][0]
            dev1 = connect_device("Android:///%s" % devs1)
            print(devs1)
            return dev1
        elif len(devs)==2:
            devs1 = devs[0][0]
            devs2 = devs[1][0]
            dev1 = connect_device("Android:///%s" % devs1)
            dev2 = connect_device("Android:///%s" % devs2)
            print(devs1,devs2)
            return dev1, dev2
        else:
            print('电脑没发现插有手机设备，如有插入手机，请检查相关端口是否被占用？')
            return False