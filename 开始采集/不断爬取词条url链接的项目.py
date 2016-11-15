from urllib import urlopen
from bs4 import BeautifulSoup
import re
import  datetime
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    url="http://en.wikipedia.org"+articleUrl
    html=urlopen(url)
    bsObj=BeautifulSoup(html)
    return bsObj.find("div",{"id":"mw-content-text"}).findAll("a",href=re.compile("^(/wiki)((?!:).)*$"))
links=getLinks("/wiki/Kevin_Bacon")
while(len(links)>0):
    newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links=getLinks(newArticle)
