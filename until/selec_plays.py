# -*- encoding=utf8 -*-
__author__ = "Administrator"
import re
from airtest.core.api import *
from poco.drivers.std import StdPoco
auto_setup(__file__)

GDcity_plays=[]
GDcity_plays_del=[]
select_people=[]
del_selected=[]
jushus=[]
del_jushus=[]
guipais=[]
del_guipais=[]
guis=[]
del_guis=[]
maimas=[]
mas_item=[]
del_mas_item=[]
rc_items=[]
del_rc_items=[]
poco = StdPoco()

class select_play:
    def getPlay(self):
        #获取二级节点item_select所有节点
        playitem_select=poco("list_view_select").child("item_select")
         #遍历二级节点item_select下所有节点
        for its in range(len(playitem_select)):
            listplay=playitem_select[its]
            print('获取到的item有:',listplay.get_text())
        #获取四级所有接点
        playitem_btn=poco("list_view_select").child("item_select").child().child("label_name")
        #遍历所有四级节点，并将其添加到全局列表GDcity_plays中
        for btn_itm in range(len(playitem_btn)):
            GDcity_plays.append(playitem_btn[btn_itm])
        print('城市',playitem_btn[btn_itm].get_text())
    #将其添加到城市玩法列表
    def append_GDcitydel(self):
        for del_pl in range(len(GDcity_plays)):
            GDcity_plays[del_pl].click()
            GDcity_plays_del.append(GDcity_plays[del_pl])
            break
    #循环删除全局列表中已选择过的玩法
    def del_GDcity(self):
        for del_cityclicked in range(len(GDcity_plays_del)):
            del GDcity_plays[del_cityclicked]
            break
    #获取玩法人数
    def getplay_people(self):
        people=poco("guizhe_ScrollView").child("<Node | Tag = -1").child("<Node | Tag = -1").child("Layout")[0].child("root").child("radio_panel").child("<Node | Tag = -1")
        for o_people in range(len(people)):
            select_people.append(people[o_people])
    #循环点击玩法后，将其添加到删除列表GDcity_plays_del中，使其下次不再点击已选择过的玩法
    def click_people(self):
        for click_people in range(len(select_people)):
            select_people[click_people].child("root").child("radio_btn").click()
            del_selected.append(select_people[click_people])
            break
    def del_clickedpeople(self):
        for del_item in range(len(del_selected)):
            del select_people[del_item]
            break
    #计算某种玩法提供的人数选择
    def count_playpeople(self):
        for countplay in range(len(select_people)):
            countplay=countplay+1
        return countplay
    #获取局数种类
    def getjushu(self):
        jushu=poco("guizhe_ScrollView").child("<Node | Tag = -1").child("<Node | Tag = -1").child("Layout")[1].child("root").child("radio_panel").child("<Node | Tag = -1")
        for o_jushu in range(len(jushu)):
            jushus.append(jushu[o_jushu])
            #调试是否获取到局数相关选项
            # print('当前获取的局数玩法有:',jushu[o_jushu].child("root").child("text").get_text())
        print('jushus has：',jushus)
    def click_jushu(self):
        for click_jushus in range(len(jushus)):
            jushus[click_jushus].child("root").child("radio_btn").click()
            del_jushus.append(jushus[click_jushus])
            break
    def del_jushu(self):
        for del_jitem in range(len(del_jushus)):
            del jushus[del_jitem]
            break
     #获取鬼牌列表中所有选项
    def get_guipai(self):
        guipais=poco("Widget").child("root")
        for guipai_item in range(len(guipais)):
            guipaiitems=guipais[guipai_item].child("Label_name").get_text()
            gui=re.search('\D鬼',guipaiitems)
            if gui!=None:
                guis.append(guipais[guipai_item])
    #点击鬼牌后，添加至待删除的鬼牌列表，避免下次点击同样位置
    def click_guipai(self):
        count1=0
        for guis_item in range(len(guis)):
            time.sleep(1)
            # if guis[guis_item]=='翻鬼':
            #     time.sleep(2)
            #     poco("Widget").child("root")[8].child("Label_name").click()
            #     del_guis.append(guipais[guipai_item])
            #     break
            guis[guis_item].click()
            del_guis.append(guis[guis_item])
            break
    def del_guis1(self):
        for del_guisitem in range(len(del_guis)):
            # print('删除的有：',guis[del_guisitem])
            del guis[del_guisitem]
            break
    #选择买马
    def maima(self):
        select_maima=poco("Widget").child("root")
        for maima_item in range(len(select_maima)):
            # maimas.append((select_maima[maima_item]).child("Label_name"))
            maimas_txt=select_maima[maima_item].child("Label_name").get_text()
            #匹配有‘马’的Label_name，不匹配标题‘买马’
            mas=re.search('无马|[1-9]马|[1-9].马$',maimas_txt)
            #将匹配到的结果，去掉为空列表，添加到mas_item
            if mas!=None:
                mas_item.append((select_maima[maima_item]).child("Label_name"))
        # print('买马',mas_item)
    def click_maima(self):
        for click_maima_item in range(len(mas_item)):
            # print('需要点击的',mas_item[click_maima_item])
            mas_item[click_maima_item].click()
            del_mas_item.append(mas_item[click_maima_item])
            break
    def del_click_maima(self):
        for delclick in range(len(del_mas_item)):
            del mas_item[delclick]
            break
     #房费选择
    def get_roomcharge(self):
        roomcharge=poco("guizhe_ScrollView").child("<Node | Tag = -1").child("<Node | Tag = -1").child("Layout")[2].child("root").child("radio_panel").child("<Node | Tag = -1")
        for rc_item in range(len(roomcharge)):
            rc_items.append(roomcharge[rc_item].child("root").child("<Sprite | Tag = -1, TextureID = 234>"))
    def click_roomcharge(self):
        for rc_items_sub in range(len(rc_items)):
            rc_items[rc_items_sub].click()
            del_rc_items.append(rc_items[rc_items_sub])
            break
    def del_click_roomcharge(self):
        for del_click in range(len(del_rc_items)):
            del rc_items[del_click]
            break
    def click_sure(self):
        poco("btn_sure").click()

