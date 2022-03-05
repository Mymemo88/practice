import csv
import pandas as pd
import math
import requests
import re
import os


#物件
def list_update():
    #get information from lastest list csv
    f=open("main.csv","r",newline="",encoding="utf-8")
    read_f=csv.reader(f)
    f_list=[row for row in read_f]
    f.close()
    
    #get information from database
    g=open("database.csv", "r", newline="",encoding="utf-8")
    read_g=csv.reader(g)
    g_list=[row for row in read_g]
    g.close()

    g=open("tmp.csv","w",newline="",encoding="utf-8")
    writer=csv.writer(g)
    writer.writerows(g_list)
    g.close()
    
    
    #compear f_list with g_list
    l_0=[row[0] for row in f_list]
    l_1=[row[1] for row in f_list]
    
    g_0=[row[0] for row in g_list]
    g_1=[row[1] for row in g_list]

    print("掲載中",len(l_0),"件")

    for ii in l_0:
        if ii in g_0:
            if len(g_list[g_0.index(ii)])<5:
                g_list[g_0.index(ii)].append("掲載中")
            else:
                print(g_list[g_0.index(ii)][4],g_1[g_0.index(ii)])
            
        else:
            print(ii," is new project")


    for ii in g_0:
        if ii in l_0:
            tt=1
        else:
            g_list[g_0.index(ii)][4]="掲載終了"
            print("掲載終了",g_list[g_0.index(ii)][1])
            
    g=open("database.csv","w",newline="",encoding="utf-8")
    writer=csv.writer(g)
    writer.writerows(g_list)
    g.close()

            
    
def table_update():
    g=open("database.csv", "r", newline="",encoding="ut\
f-8")
    read_g=csv.reader(g)
    g_list=[row for row in read_g]
    g.close

    g_0=[row[0] for row in g_list]
    g_1=[row[1] for row in g_list]
    f=open("../shared/Download/test.md","w")
    f.write("# Project table  \n")
    f.write("  \n")
    f.write("### 販売中  \n")
    f.write("  \n")
    f.write("No.|name|note  \n")
    f.write("---|---|---  \n")
    for ii, row in enumerate(g_0):
        if g_list[ii][4]=="掲載中":
            f.write(g_0[ii])
            f.write("|")
            f.write(g_1[ii])
            f.write("| \n")
        
    f.write("  \n")
    f.write("### 販売終了  \n")
    f.write("  \n")
    f.write("No.|name|note  \n")
    f.write("---|---|---  \n")
    for ii, row in enumerate(g_0):
        if g_list[ii][4]=="掲載終了":
            f.write(g_0[ii])
            f.write("|")
            f.write(g_1[ii])
            f.write("| \n")
            
    f.close()
    
    
#物件サイトからデータ抽出し、CSVを作成
from bs4 import BeautifulSoup
def mkcsv(url):
     site=requests.get(url)
     data=BeautifulSoup(site.content,"html.parser")
     table=data.find("table")
     rows=table.find_all("tr")
     pattern=".info/\d+/outline"
     r=re.search(pattern,url)
     rr=r.group()
     xx=re.sub("\D","",rr)
     csvFile=open("project_csv/"+xx+".csv", "wt", newline="", encoding="utf-8")
     writer=csv.writer(csvFile)

     try:
         for row in rows:
             csvRow=[]
             for cell in row.find_all(["td", "th"]):
                 csvRow.append(cell.get_text())
                
             writer.writerow(csvRow)
     finally:
         csvFile.close()


def all_update():
    g=open("database.csv", "r", newline="",encoding="utf-8")
    read_g=csv.reader(g)
    g_list=[row for row in read_g]
    g.close()

    g_0=[row[0] for row in g_list]
    g_1=[row[1] for row in g_list]
    g_2=[row[2] for row in g_list]
    g_3=[row[3] for row in g_list]

    for ii, jj in enumerate(g_3):
        if jj=="":
            print(ii)
            print(g_1[ii]," has no detail.")
        else:
            print(g_1[ii])
            mkcsv(jj)
            
