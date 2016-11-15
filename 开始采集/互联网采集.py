from urllib import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#get list of all inner links
def getInnerLinks(bsObj,includeUrl):
    innerLinks=[]#list
    #find all links which start with "/"
    for link in bsObj.findAll("a",href=re.compile("^(/\.*"+includeUrl+")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in innerLinks:
                innerLinks.append(link.attrs["href"])#add item
    return innerLinks

# get list of all outter links
def getExternalLinks(bsObj,excludeUrl):
    externalLinks=[]
    #find all external links start with "http" or "www"
    for link in bsObj.findAll("a",
                              href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):#E.g  don't include ^(http|www)((?!oreilly.com).)*$
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks

def splitAddr(addr):
    addrParts=addr.replace("http://","").split("/")
    return addrParts

def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bsObj=BeautifulSoup(html)
    externalLinks=getExternalLinks(bsObj,splitAddr(startingPage)[0])
    if len(externalLinks)==0:
        innerLinks=getInnerLinks(bsObj,)
        return getExternalLinks(innerLinks[random.randint(0,len(innerLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink=getRandomExternalLink("http://oreilly.com")
    print("Random external Link is :"+externalLink)
    followExternalOnly(externalLink)

#collect all external links list
allExternalLinks=set()
allInnerLinks=set()
def collect(siteUrl):
    global allExternalLinks
    global allInnerLinks
    html = urlopen(siteUrl)
    bsObj=BeautifulSoup(html)
    innerLinks=getInnerLinks(bsObj,splitAddr(siteUrl)[0])
    externalLinks=getExternalLinks(bsObj,splitAddr(siteUrl)[0])
    for link in externalLinks:
        if link not in allExternalLinks:
            allExternalLinks.add(link)
            print("*****Getting external Link: "+link)
    for link in innerLinks:
        if link not in allInnerLinks:
            allInnerLinks.add(link)
            print("-----Getting inner Link: "+link)
            collect(link)

collect("http://oreilly.com")
#followExternalOnly("http://oreilly.com")
