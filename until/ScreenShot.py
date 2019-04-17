#coding=utf-8
from BeautifulReport import BeautifulReport
from selenium import webdriver
import os
class ScreenShot():
    def save_Shotimg(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(('../img')),img_name))
