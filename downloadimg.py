# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 21:35:23 2018

@author: Chengbi
"""
import pandas as pd
import urllib

def downloadimg(csv):
    try:
        df=pd.read_csv(csv,encoding='utf-8')
    except:
        df=pd.read_csv(csv,encoding='latin-1')
    i=0
    for item in df.picurl:
        print(i)
        urllib.request.urlretrieve(item, "C:/Users/Chengbi/OneDrive - George Mason University/Research/WebScraper/images/{!s}.png".format(item[-10:])) 
        i+=1
downloadimg("new1.csv")