import time, requests
from bs4 import BeautifulSoup
import csv, datetime, os
r = requests.get('https://www.blackrock.com/us/individual/products/239726/ishares-core-sp-500-etf').content
soup = BeautifulSoup(r,'html.parser')
date = soup.find('span',{'class':'header-nav-label navAmount'}).text.strip().split('of')[1]
fdate = datetime.datetime.strptime(date,' %b %d, %Y').strftime('%Y%m%d')
print(fdate)
if not os.path.exists('BlackRock_US_Daily_Nav_' + fdate + '.csv'):
    csvfile = open('BlackRock_US_Daily_Nav_' + fdate + '.csv','a',newline='\n')
    filewriter = csv.writer(csvfile)
    filewriter.writerow(['Date','Fund Name','Ticker','NAV'])
    file = open('blackrock_links.txt','r')
    for link in file:
        r = requests.get(link.split('\n')[0]).content
        soup = BeautifulSoup(r,'html.parser')
        ticker = soup.find('div',{'class':'identifier-wrapper'}).text.strip()
        nav = soup.find('span',{'class':'header-nav-data'}).text.strip()
        date = soup.find('span',{'class':'header-nav-label navAmount'}).text.strip().split('of')[1]
        fundname = soup.title.text.split('|')[0]
        print(date,fundname,ticker,nav)
        filewriter.writerow([fdate,fundname,ticker,nav])
else:
    print('File Already Exists')