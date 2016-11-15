from urllib import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html)
    for link in bsObj.find("div",{"id":"mw-content-text"}).findAll("a",href=re.compile("^(/wiki)((?!:).)*$")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                newPage=link.attrs["href"]
                print (newPage)
                pages.add(newPage)
                getLinks(newPage)#recursion
getLinks("")#start with home page "http://en.wikipedia.org"