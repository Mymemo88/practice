import requests
import csv
import re
from bs4 import BeautifulSoup
site=requests.get("https://www.wadakohsan.co.jp/\
index.html") 
#get all infromation from target site.


data=BeautifulSoup(site.content,"html.parser")
cont1=data.find(id="container")
#get "container" part information from target.

tmplist=list()
#list for project name

tmplist2=list() 
#list for project official URL.

#make "tmplist1, 2"
for element in cont1.find_all("h3"):
    element2=element.find("strong")
    tmplist.append(element2.string)
    url=element.find("a").get("href")
    tmplist2.append(url)
    print(element2.text)
    

tmplist3=list()

for x in tmplist2:
    site=requests.get(x)
    data=BeautifulSoup(site.content,"html.parser")
    cont1=data.find("header")
    cont2=list()
    cont3=list()
    try:
        cont2=cont1.find_all("a")
        for y in cont2:
            cont3.append(y.get("href"))
        for y in cont3:
            if "outline.php" in y:
                break
    except AttributeError:
        y=None
    tmplist3.append(y)
    

tmplist4=list()
pattern=".info/\d+/outline"
for i, x in enumerate(tmplist3):
    try:
        r=re.search(pattern,tmplist3[i])
        rr=r.group()
        xx=re.sub("\D","",rr)
    except TypeError:
        xx=None
    tmplist4.append(xx)


csvFile=open("main.csv","w",newline="",encoding="utf-8")
writer=csv.writer(csvFile)
for i, x in enumerate(tmplist):
    writer.writerow([tmplist[i],tmplist2[i],tmplist3[i],tmplist4[i]])
                    
