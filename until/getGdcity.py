# -*- encoding=utf8 -*-
__author__ = "Administrator"
from airtest.core.api import *
auto_setup(__file__)
from poco.drivers.std import StdPoco
poco = StdPoco()
GDcity = []
GDcity_del = []
class Gd:
    def getGDcitylist(self):
        GDcitysroot = poco("city_list").child("root")  # 获取广东地区二级节点root
        for roots in range(len(GDcitysroot)):
            roots_btn = GDcitysroot[roots].child()  # 获取三级节点
            count = 0
            for btn in range(len(roots_btn)):  # 遍历每个二级节点的子节点
                citys = roots_btn[btn].child("city_name")  # 获取城市名称
                GDcity.append(citys)
    def countGDcity(self):
        for countC in range(len(GDcity)):
            countC = countC + 1
        # print('共计城市:',countC)
        return countC

    def clickcity(self):
        for cityname in range(len(GDcity)):
            GDcity[cityname].click()
            GDcity_del.append(GDcity[cityname])
            # print('第%d次往GDcity_del中添加名称为:%s' % (cityname, GDcity_del))
            break
    def removecity(self):
        for del1 in range(len(GDcity_del)):
            del GDcity[del1]
            # print('第%d次删除的城市名称有:%s' % (del1, GDcity))
            break