#coding=utf-8
from  base64 import b64decode
from poco.drivers.std import StdPoco
class snapscreen():
    def snaps(self):
        poco=StdPoco()
        b64,fmt=poco.snapshot(width=720)
        savescreen=open('D:\\work\\abc\\{}.png'.format(fmt),'wb').write(b64decode(b64))