import time,datetime,os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
driver = webdriver.Chrome()
driver.get('https://www.fidelity.ca/fidca/en/priceandperformance?view=AG')
time.sleep(10)
date = driver.find_element_by_xpath('//*[@id="sticker"]/thead/tr[1]/td[2]/span').text.strip()
fdate = datetime.datetime.strptime(date,'%d-%b-%Y').strftime('%Y%m%d')
print(fdate)
if not os.path.exists('Fidelity_Daily_Nav_'+fdate+'.csv'):
    for i in range(2,12):
        driver.find_element_by_xpath('//*[@id="aria_trigger_3"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="aria_target_3"]/li['+str(i)+']/button').click()
        name = driver.find_element_by_xpath('//*[@id="aria_trigger_3"]').text
        print(name)
        time.sleep(30)
        if name not in ['ETF only','Series C','Series D']:
            driver.find_element_by_xpath('//*[@id="aria_trigger_4"]').click()
            time.sleep(4)
            driver.find_element_by_xpath('//*[@id="aria_target_4"]/li[1]/button').click()
            time.sleep(30)
            driver.find_element_by_xpath('//*[@id="aria_trigger_5"]').click()
            time.sleep(4)
            driver.find_element_by_xpath('//*[@id="aria_target_5"]/li[1]/button').click()
            time.sleep(4)
        soup = BeautifulSoup(driver.page_source,'html.parser')
        Table = soup.find('table', {"class":"listing pnp body collapsible has_action_menus view_AG"})
        df1 = pd.read_html(str(Table))[0]
        df2 = df1.iloc[:,[0,2]]
        ticker = []
        for tic in df2.iloc[:,0].values:
            if '(' in str(tic):
                ticker.append((tic).split('(')[1].replace(')',""))
            elif 'Ticker' in str(tic):
                ticker.append((tic).split('Ticker')[1])
            else:
                ticker.append("")
        filename = open('Fidelity_Daily_Nav_'+fdate+'.csv',"a", newline="\n")
        csv_writer = csv.writer(filename)
        csv_writer.writerow(['Date', 'Fund Name', 'Ticker', 'NAV'])
        filename.close()
        df2.insert(0, 'Date', fdate)
        df2.insert(2, 'Ticker', pd.Series(ticker))
        df2.to_csv('Fidelity_Daily_Nav_'+fdate+'.csv',mode='a',index=False,header=False)
    driver.close()
else:
    print('File Already Exists')