# Import necessary Library:
import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime                       # datetime library


# How to scrap data from a website and use of datetime library:

lis_api = []
lis_name = [] 
beyond48hour = 0
pageno = 0
while beyond48hour == 0:
    print(pageno)
    payload = {}
    payload['page'] = pageno
    url = 'https://data.gov.in/ogpl_apis'
    page = requests.get(url, payload)
    soup = BeautifulSoup(page.text)
    pageno = pageno + 1
#     lis_api = []
#     lis_name = [] 
    data = soup.find_all('div', attrs={"class":"apifrom_dataset"})
    for i in range(len(data)):
        #temp = []
        heading = data[i].find_all('a')[0].get_text()
        link = data[i].a.get('href')
        time = data[i].find('div', attrs= { 'class':"updated_date"}).find('span', attrs ={ 'class':"count-datasets"}).text 
        datetime_str = datetime.datetime.strptime(time, ' %d/%m/%Y %I:%M:%S %p') 
        time_for_today = datetime.datetime.today()
        if (time_for_today - datetime_str).total_seconds() < 172800 :
            lis_api.append( str(i)+ ' '+ link )
            lis_name.append(str( i) +' ' + heading)
        else:
            beyond48hour = 1 
