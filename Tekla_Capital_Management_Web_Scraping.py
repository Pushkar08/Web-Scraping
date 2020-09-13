import requests
import csv,os,datetime
import pandas as pd
from bs4 import BeautifulSoup
links = ['hqh','hql','thq','thw']
r = requests.get('https://www.teklacap.com/funds/hqh/fund/fund-information/').content
soup = BeautifulSoup(r,'html.parser')
date = soup.find_all("table", {"class": "styled-table-1"})[3].text.split()[2]
fdate = datetime.datetime.strptime(date,'%m/%d/%Y').strftime('%Y%m%d')
print(fdate)
if not os.path.exists('Tekla_Capital_Management_Daily_Nav_' + fdate + '.csv'):
    csvfile = open('Tekla_Capital_Management_Daily_Nav_' + fdate + '.csv', 'a', newline='\n')
    filewriter = csv.writer(csvfile)
    filewriter.writerow(['Date','Fund Name','Ticker','NAV'])
    for link in links:
        r = requests.get('https://www.teklacap.com/funds/'+str(link)+'/fund/fund-information/').content
        soup = BeautifulSoup(r,'html.parser')
        nav = soup.find_all("table", {"class": "styled-table-1"})[3].text.split()[4]
        fundname = soup.find("div", {"class": "fund-header__fund-name"}).find('a').text.split('(')[0]
        ticker = soup.find("div",{"class":"fund-header__fund-name"}).find('a').text.split('(')[1].replace(')',"")
        filewriter.writerow([fdate,fundname,ticker,nav])
else:
    print('File Already Exists')