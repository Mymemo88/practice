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

    #compear f_list with g_list
    l_0=[row[0] for row in f_list]
    l_1=[row[1] for row in f_list]
    
    g_0=[row[0] for row in g_list]
    g_1=[row[1] for row in g_list]

    for ii in l_0:
        if ii in g_0:
            print("exist ", g_1[g_0.index(ii)])
            
        else:
            print(ii," is not exist")
        
    
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
    f.write("###販売中  \n")
    f.write("  \n")
    f.write("No.|name|note  \n")
    f.write("---|---|---  \n")
    for ii, row in enumerate(g_0):
        f.write(g_0[ii])
        f.write("|")
        f.write(g_1[ii])
        f.write("| \n")
            
    f.close()
    
    
