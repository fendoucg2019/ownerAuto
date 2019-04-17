#coding=utf-8
from selenium import webdriver
from airtest.core.api import *
from poco.drivers.std import StdPoco
import random
import unittest
kfwebchat=''.join(str(i) for i in random.sample(range(0,9),5))
class qinyouhoutai(unittest.TestCase):
    #获取用户ID
    def get_id(self):
        from until.ChangeDevs import ChangeDev
        selectDev = ChangeDev()
        selectDev.changedev()
        set_current(1)
        poco = StdPoco()
        userid = poco("lb_id").get_text().split(':')[1]
        return userid
    #定义判断web元素是否存在
    def isElementExist(self, element):
        flag = True
        browser = self.browser
        try:
            browser.find_element_by_xpath(element)
            return flag
        except:
            flag = False
            return flag
    def open_qinyouhoutai(self):
        # display=Display(visible=0,size=(1920,1080))
        # display.start()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        urllink = 'http://120.78.199.18:38080/club_admin/index'
        self.browser.get(urllink)
        admininput = self.browser.find_element_by_name("userName")
        admininput.send_keys('admin')
        passwordinput = self.browser.find_element_by_id("password")
        passwordinput.send_keys('123456')
        login = self.browser.find_element_by_xpath('//*[@id="frmSignIn"]/div[4]/div[3]/input')
        login.click()
        time.sleep(0.5)
        openguangdlink=self.browser.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/button')
        openguangdlink.click()
        time.sleep(0.5)
        self.browser.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[1]/a').click()
        time.sleep(0.5)
        self.browser.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[1]/ul/li[1]/a/span').click()
        time.sleep(0.5)
        inputid=self.get_id()
        self.browser.find_element_by_xpath('//*[@id="playId"]').send_keys(inputid)
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="sub"]').click()
        time.sleep(0.5)
        gly=self.isElementExist('/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/h3')
        if gly:
            self.browser.close()
        else:
        # ktqy=browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/input')
        # if len(ktqy)==0:           #browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/input')
        #     return False
        # if len(ktqy)==1:
            time.sleep(0.5)
            self.browser.find_element_by_id('inCellPhone').send_keys('13760276826')
            self.browser.find_element_by_id('staffWechat').send_keys(kfwebchat)
            username=''.join(chr(a) for a in random.sample(range(97,123),5))
            time.sleep(0.5)
            self.browser.find_element_by_id('inRealName').send_keys(username)
            time.sleep(0.5)
            self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/input').click()
            time.sleep(0.5)
            self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[2]/div/div/form/table[2]/tbody/tr/td[1]/input').click()
            time.sleep(0.5)
            self.browser.close()
