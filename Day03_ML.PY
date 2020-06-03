import pandas as pd
import matplotlib as plt
>> pd.DataFrame([1,2,3])
   0
0  1
1  2
2  3
>>> df=pd.DataFrame([1,2,3])
>>> df[0]
0    1
1    2
2    3
Name: 0, dtype: int64

dct={'name':[],'marks':[]}
>>> dct={'name':['A','B','C'],'marks':[90,80,70]}
>>> df=pd.DataFrame(dct)
>>> df
  name  marks
0    A     90
1    B     80
2    C     70

 import matplotlib.pyplot as plt
>>> plt.bar(df['name'],df['marks'])
<BarContainer object of 3 artists>
>>> plt.show()

plt.bar(df['name'],df['marks'])
<BarContainer object of 3 artists>
>>> plt.show()
>>> data={1:df,2:df}
>>> p=pd.Panel(data)

>>> p=pd.Panel()
>>> p
<pandas.Panel object at 0x7f27e9ca18d0>
>>> s=pd.Series{[1,2,3,4],index=[100,101,102,103]}
 
>>> s=pd.Series([1,2,3,4],index=[100,101,102,103])
>>> s
100    1
101    2
102    3
103    4
dtype: int64


>>> p=pd.Panel()
>>> p
<pandas.Panel object at 0x7f27e9ca16d8>
>>> data
{1:   name  marks
0    A     90
1    B     80
2    C     70, 2:   name  marks
0    A     90
1    B     80
2    C     70}

# HOW TO SAVE DATASET THAT WE HAVE DOWNLOADED FROM NET DIRECTLY
>>> df.to_csv('batch2.csv')
>>> df=pd.read_csv('https://raw.githubusercontent.com/datasets/breast-cancer/master/data/breast-cancer.csv')
>>> df.to_csv('b2.csv')

import requests
page=requests.get('https://www.google.com')
page.status_code
200
 
 #TO GET HTML CODE IN AN ORGANISED WAY OF ANY WEBPAGE

from bs4 import BeautifulSoup
page=requests.get('https://www.amazon.in/CHANAKYA-NEETI-R-P-Jain-ebook/dp/B01FAWGHAO/ref=pd_rhf_cr_s_zg_ebk_1_1/261-2849361-5851257?_encoding=UTF8&pd_rd_i=B01FAWGHAO&pd_rd_r=e92281ad-767e-4977-aff7-460c60fde85b&pd_rd_w=GLJxB&pd_rd_wg=iLdaI&pf_rd_p=6ae19939-ecb3-4591-9f68-18223252d6cd&pf_rd_r=D679YQN283T835SBW28T&psc=1&refRID=D679YQN283T835SBW28T',
                  headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.8'})
print(page.status_code)

soup=list(soup.children)[11]
html=list(soup.children)[10]
type(html)
list(html.children)

##import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
##page=requests.get('https://www.amazon.in/',
##                  headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',})
##soup=BeautifulSoup(page.content,'html.parser')
##html=list(soup.children)[10]
##body=list(html.children)[3]
##msg=body.findAll('p')
##final_msg=msg[0].get_text()
##print(final_msg)
##


#Fetch from url using requests.get()
#Create a soup using BeautifulSoup()
#get children and its element until you find your final desirable output,known as ResultSet
#apply rs[index].get_text() method to get desired text content


page2=requests.get('https://mausam.imd.gov.in/')
soup=BeautifulSoup(page2.content,'html.parser')
html=list(soup.children)[3]
body=list(html.children)[3]
divs=body.findAll('div')
tem=divs[0].findAll(id="temperature")
hum=divs[0].findAll(id="temperature1")
air=soup.findAll('li',class_="sun-info")
##print('Delhi Weather')
##print('Temperature', tem[0].get_text())
##print('Humidity',hum[0].get_text())
##print('Air Flow: ',air[0].get_text())
today=soup.find_all('div',class_='capital')
data=[]
dataframe=[]
places=[]
for i in today:
    data.append(i)
for j in range(len(data)):
    cities=today[j].find_all('h3')
    city=[city.get_text() for city in cities]
    temp=today[j].find_all('p',class_="now")
    temps=[temps.get_text() for temps in temp]
    places.append(temps)
    wind=today[j].find_all('p',class_="wind")
    wind_direction=[winds.get_text() for winds in wind]
    humidity=today[j].find_all('p',class_="minmax")
    today_humidity=[hum.get_text() for hum in humidity]
    print(city,temps,wind_direction,today_humidity)

