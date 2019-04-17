#coding=utf-8
from airtest.core.android.android import Android
from airtest.core.android.adb import ADB
import time
from poco.drivers.std import StdPoco
adb=ADB()
class getDevices:
    def getDe(self):
        getD=adb.devices()
        if getD:
            print('当前设备为',getD)
        else:
            adb.kill_server()
            adb.start_server()
            print('当前无设备，请连接设备')
            raise IndexError("ADB devices not found")
            return getD
class starts:
    def startPackage(self):
        android = Android()
        android.start_app('com.dashengzhangyou.pykf.lailaiguangdong')
        time.sleep(5)




