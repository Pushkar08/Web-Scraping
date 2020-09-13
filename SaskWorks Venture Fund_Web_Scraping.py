import requests
import csv,os,datetime
from bs4 import BeautifulSoup
r = requests.get('https://www.saskworks.ca/diversified-share-class/performance/').content
soup = BeautifulSoup(r,'html.parser')
date = soup.find("span", {"class": "border"}).text.split('at')[1]
fdate = datetime.datetime.strptime(date,' %B %d, %Y').strftime('%Y%m%d')
print(fdate)
if not os.path.exists('SaskWorks Venture Fund Inc._Daily_Nav_'+fdate+'.csv'):
    filename = open('SaskWorks Venture Fund Inc._Daily_Nav_'+fdate+'.csv', "a", newline="\n")
    csv_writer = csv.writer(filename)
    csv_writer.writerow(['Date','Fund Name','Nav'])
    fundname1 = soup.find_all("span", {"class": "blue"})[0].text.split('$')[0]
    nav1 = soup.find_all("span", {"class": "blue"})[0].text.split('$')[1]
    fundname2 = soup.find_all("span", {"class": "blue"})[1].text.split('$')[0]
    nav2 = soup.find_all("span", {"class": "blue"})[1].text.split('$')[1]
    fundname3 = soup.find_all("span", {"class": "green"})[0].text.split('$')[0]
    nav3 = soup.find_all("span", {"class": "green"})[0].text.split('$')[1]
    fundname4 = soup.find_all("span", {"class": "green"})[1].text.split('$')[0]
    nav4 = soup.find_all("span", {"class": "green"})[1].text.split('$')[1]
    csv_writer.writerow([fdate,fundname1,nav1])
    csv_writer.writerow([fdate,fundname2,nav2])
    csv_writer.writerow([fdate,fundname3,nav3])
    csv_writer.writerow([fdate,fundname4,nav4])
else:
    print('File Already Exists')