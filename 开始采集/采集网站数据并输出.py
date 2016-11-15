from urllib import urlopen
from bs4 import BeautifulSoup
import re

pages=set()
def getLinks(pageUrl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html)
    try:
        print(bsObj.h1.get_text())
        p1=bsObj.find(id="mw-content-text").findAll("p")[0]
        print(p1.get_text())
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("page has lost some attributes, but don't worry!")

        for link in bsObj.findAll("a",href=re.compile("^(/wiki)((?!:).)*$")):
            if "href" in link.attrs:
                if link.attrs["href"] not in pages:
                    newPage=link.attrs["href"]
                    pages.add(newPage)
                    print("*****************\n"+newPage)
                    getLinks(newPage)

getLinks("")
