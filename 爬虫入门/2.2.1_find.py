#coding:utf-8
from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

def getName(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        print e.code
        print e.reason
        return None
    try:
        bsObj=BeautifulSoup(html.read().decode('gbk').encode('utf-8'))
        nameList=bsObj.findAll("div",{"class":"hotnews"})
        return nameList
    except AttributeError as ee:
        return None

url="http://news.baidu.com/"
nameList=getName(url)

for name in nameList:
    print (name.get_text())

