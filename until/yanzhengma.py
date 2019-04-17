#coding=utf-8
import requests
def yzm():
    play={'1.'}
    r=requests.get('http://120.78.199.18:18105/test/code?phone=13711111111',params=play)
    s=r.text.split(':')[1]
    s1=s.split('.')[1]
    s2=s1.split('<')[0]
    return s2.strip()