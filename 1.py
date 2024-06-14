import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import time
import os
import pandas as pd
import numpy as np

#list1=['宸美（厦门）光电有限公司']
list1=open('company_name.txt','r',encoding='utf-8').readlines()
headers = {
	'Cookie':'HWWAFSESID=0bfe61274db43996e98; HWWAFSESTIME=1718327347052; csrfToken=vSQe57CDFv6i5mn4ZGBqKNmP; TYCID=b3a81d4029ea11efaed66da2b9abc5b5; CUID=459fa22f157527823fa02f38435d05a5; ssuid=248993856; sajssdk_2015_cross_new_user=1; bannerFlag=true; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1718250695,1718327367; _ga=GA1.2.74891638.1718327368; _gid=GA1.2.1878453369.1718327368; tyc-user-info={%22state%22:%220%22%2C%22vipManager%22:%220%22%2C%22mobile%22:%2217859730580%22%2C%22userId%22:%22335066870%22}; tyc-user-info-save-time=1718327944240; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzg1OTczMDU4MCIsImlhdCI6MTcxODMyNzk0NSwiZXhwIjoxNzIwOTE5OTQ1fQ.S9KlDR-WaM_hbQPZz7ZAVtYWS90IRBOxjcdPDXngvQlyo2MB2AM6YhoO1fBoa9Vr7gJvmAOUghpi0vD1VMOaVg; tyc-user-phone=%255B%252217859730580%2522%255D; searchSessionId=1718328713.69394208; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22335066870%22%2C%22first_id%22%3A%22190144acf211f6-03853b7ccdec79a-4c657b58-2073600-190144acf2267d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwMTQ0YWNmMjExZjYtMDM4NTNiN2NjZGVjNzlhLTRjNjU3YjU4LTIwNzM2MDAtMTkwMTQ0YWNmMjI2N2QiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIzMzUwNjY4NzAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22335066870%22%7D%2C%22%24device_id%22%3A%22190144acf211f6-03853b7ccdec79a-4c657b58-2073600-190144acf2267d%22%7D; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1718344434',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}

tx=''

def get_url(company):
    url = 'https://www.tianyancha.com/search?key={}'.format(quote(company))
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    #print(soup)
    info = soup.select('.index_header__x2QZ3 .index_name__qEdWi a')[0]
    company_url = info['href']
    return company_url

def get_data(url,company):
    while True:
        try:
            html2 = requests.get(url,headers=headers)
            soup2 = BeautifulSoup(html2.text,'lxml')
            info = soup2.select('.index_detail-info-item__oAOqL span')
        except:
            os.system("pause")
            continue
        break
            
    
    tx1=company
    for ind in range(len(info)):
        #print(info[ind])
        try:
            litter=info[ind].text
            
        except:
            litter=info[ind].string
        tx1+='  '+litter

    tx1+='\n'
    return tx1
    #print(info)
    #return company_url

def pd_df(company,company_data):
    pass
    

for company in list1:
    company=company.strip()
    while True:
        try:
            company_url=get_url(company)
        except:
            os.system("pause")
            continue
        break
    tx1=get_data(company_url,company)
    #tx+=tx1
    print(company)
    
    with open('data1.txt','a',encoding='utf-8') as f:
        f.write(tx1)

print('ok')
