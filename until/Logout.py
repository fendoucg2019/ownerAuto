#coding=utf-8
from airtest.core.api import *
from poco.drivers.std import StdPoco
from until.ChangeDevs import ChangeDev
class Logouts():
    def Logout(self):
        time.sleep(1)
        dev=ChangeDev()
        dev.changedev()
        set_current(1)
        poco = StdPoco()
        keyevent("BACK")
        poco("btn_yes").click()