import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content,'html.parser')
seven_day = soup.find(id='seven-day-forecast')
forecast_items = seven_day.find_all(class_="tombstone-container")
#today = forecast_items[0]

Time=[]
Short_descs=[]
Descriptions=[]
Temperatures=[]
for today in forecast_items:
    period =Time.append(today.find(class_='period-name').get_text())
    short_desc = Short_descs.append(today.find(class_='short-desc').get_text())
    try:
        temp = Temperatures.append(today.find(class_="temp temp-low").get_text())
    except:
        temp = Temperatures.append(today.find(class_="temp temp-high").get_text())
    #print(period)
    #print(short_desc)
   # print(temp)
    img = today.find("img")
    desc = Descriptions.append(img['title'])


weather = pd.DataFrame({
    "Time": Time,
    "Short_desc": Short_descs,
    "Descriptions":Descriptions,
    "Temperatures":Temperatures
})
print(weather)

import time
current=int(time.time())
filename='Analysis_'+str(current)
weather.to_csv(filename, index=False)

