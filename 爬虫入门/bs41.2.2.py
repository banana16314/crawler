from urllib2 import urlopen
from urllib2 import HTTPError
#import urllib2
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print e.code#code eg.403 404
        print e.reason#Forbidden Not found
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as ee:
        return None
    return title

url = "http://blog.csdn.net/"
title = getTitle(url)
if title == None:
    print("Title not found")
else:
    print(title)
