#coding=utf-8
import unittest
from airtest.core.api import *
from driver.startAPP import starts
from poco.exceptions import PocoNoSuchNodeException
weixin=starts()
weixin.startPackage()
time.sleep(5)
from poco.drivers.std import StdPoco
poco=StdPoco()
class webchatLogins(unittest.TestCase):
    def setUp(self):
        pass
    def test_weixin(self):
        try:
            assert poco("<Node | Tag = -1").child("<LayerColor | Tag = -1>")[1].child("Widget")[1].exists
            time.sleep(1)
            keyevent("BACK")
            time.sleep(0.5)
            poco("btn_login").click()
        except PocoNoSuchNodeException:
            raise(PocoNoSuchNodeException,'界面没有此元素')
    def tearDown(self):
        pass

