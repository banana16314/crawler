from bs4 import BeautifulSoup
import re
import pymysql
from urllib import urlopen

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="0318",
    db="wikipedia",
    charset="utf8"
)
cur = conn.cursor()
cur.execute("USE wikipedia")


def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url=%s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s", (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links (fromPageId,toPageId) VALUES (%s,%s)", (int(fromPageId), int(toPageId)))
        conn.commit()

pages = set()

def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a",
                              href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs["href"]))
        if link.attrs["href"] not in pages:
            newPage = link.attrs["href"]
            pages.add(newPage)
            getLinks(newPage, recursionLevel + 1)


getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()
