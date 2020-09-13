import time,csv,os,datetime
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Firefox()
driver.get('https://www.westernsouthern.com/touchstone/mutual-funds/flexible-income-fund')
date = driver.find_element_by_xpath('/html/body/main/section[3]/div/div/div[1]/div[3]/span').text
fdate = datetime.datetime.strptime(date,'%m/%d/%Y').strftime('%Y%m%d')
print(fdate)
if not os.path.exists('Touchstone_Funds_Daily_Nav_'+fdate+'.csv'):
    filename = open('Touchstone_Funds_Daily_Nav_'+fdate+'.csv',"a", newline="\n")
    csv_writer = csv.writer(filename)
    csv_writer.writerow(['Date','Fund Name','Ticker','Nav'])
    other_links = ['https://www.westernsouthern.com/touchstone/mutual-funds/anti-benchmark-international-core-equity-fund','https://www.westernsouthern.com/touchstone/mutual-funds/anti-benchmark-us-core-equity-fund']
    for links in other_links:
        driver.get(links)
        try:
            time.sleep(5)
            fundname = driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[1]/h1').text
            nav = driver.find_element_by_xpath('//*[@id="main"]/section[3]/div/div/div[1]/div[2]/div[1]/span[2]').text
            ticker=driver.find_element_by_xpath('//*[@id="main"]/section[4]/div/div/table/tbody/tr[1]/td[2]').text
            ticker1=driver.find_element_by_xpath('//*[@id="main"]/section[4]/div/div/table/tbody/tr[1]/td[3]').text
            csv_writer.writerow([fdate,fundname,ticker,nav])
            csv_writer.writerow([fdate,fundname,ticker1,nav])
        except:
            time.sleep(5)
            fundname = driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[1]/h1').text
            nav = driver.find_element_by_xpath('//*[@id="main"]/section[3]/div/div/div[1]/div[2]/div[1]/span[2]').text
            ticker=driver.find_element_by_xpath('/html/body/main/section[4]/div/div/table/tbody/tr[1]/td[2]/span').text
            ticker1=driver.find_element_by_xpath('//*[@id="main"]/section[4]/div/div/table/tbody/tr[1]/td[3]/span').text
            csv_writer.writerow([fdate,fundname,ticker,nav])
            csv_writer.writerow([fdate,fundname,ticker1,nav])

    file = open('touchstone.txt','r')
    for links in file:
        driver.get(links)
        time.sleep(7)
        soup = BeautifulSoup(driver.page_source,'lxml')
        length = len(soup.find("select", {"id": "ws-share-class__selector-main"}).findAll("option"))
        for i in range(1,length+1):
            time.sleep(3)
            try:
                driver.find_element_by_xpath('//*[@id="ws-share-class__selector-main"]').click()
                time.sleep(4)
                driver.find_element_by_xpath('//*[@id="ws-share-class__selector-main"]/option['+str(i)+']').click()
                time.sleep(4)
                fundname = driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[1]/h1').text
                nav = driver.find_element_by_xpath('//*[@id="main"]/section[3]/div/div/div[1]/div[2]/div[1]/span[2]').text
                ticker = driver.find_element_by_xpath('//*[@id="main"]/div[4]/div/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
                print(fundname,ticker,date,nav)
                csv_writer.writerow([fdate,fundname,ticker,nav])
            except:
                time.sleep(3)
                fundname = driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[1]/h1').text
                nav = driver.find_element_by_xpath('//*[@id="main"]/section[3]/div/div/div[1]/div[2]/div[1]/span[2]').text
                date = driver.find_element_by_xpath('//*[@id="main"]/section[3]/div/div/div[1]/div[3]/span').text
                ticker = driver.find_element_by_xpath('//*[@id="main"]/div[4]/div/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
                print(fundname, ticker, date, nav)
                csv_writer.writerow([fdate,fundname,ticker,nav])