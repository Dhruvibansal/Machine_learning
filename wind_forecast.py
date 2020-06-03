import requests
from bs4 import BeautifulSoup
page2=requests.get('https://mausam.imd.gov.in/',headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    })
soup = BeautifulSoup(page2.content,'html.parser')
html=list(soup.children)[3]
body=list(html.children)[3]
divs=body.findAll('div')
tem=divs[0].findAll(id="temperature")
hum=divs[0].findAll(id="temperature1")
weather=body.findAll(id="city_weather")
wind=weather[0].findAll('li')
t=weather[0].findAll('small')
air=wind[0].getText()
todayTemp=tem[0].getText()
todayHum=hum[0].getText()
time=t[0].getText()
#print("Delhi's Weather")
#print("Temperature",todayTemp)
#print("Humidity", todayHum)
#print("Wind Flow:",air)
#print(time)

#OUTPUT
#Delhi's Weather
#Temperature  36oC
#Humidity  41%
#Wind Flow:  Northwesterly 9.3 km/h
#Observation time : 2020-06-03 14.30 IST 
today=soup.find_all('div',class_='capital')
data=[]
dataframe=[]
places=[]
for i in today:
	data.append(i)
for j in range(len(data)):
	cities=today[j].find_all('h3')
	city=[city.get_text()for city in cities]
#today[0]
	temp=today[j].find_all('now')
	temps=[temp.get_text() for temps in temp]

#today[0].find_all('h3')
	wind=today[j].find_all('p', class_="wind")
	wind_direction=[winds.get_text() for winds in wind]
	humidity=today[j].find_all('p',class_='minmax')
	today_humidity=[hum.get_text() for hum in humidity]
	print(city,temps,wind_direction,today_humidity)

#OUTPUT
#['Mumbai '] [] ['Northerly 14.7km/h'] [' 88%']
#['Bengaluru '] [] ['Southwesterly 7.5km/h'] [' ']
#['Chennai '] [] ['Easterly 14.7km/h'] [' 47%']
#['Hyderabad '] [] ['South-southwesterly 9.3km/h'] [' 48%']
#['Kolkata '] [] ['West-southwesterly 5.4km/h'] [' 57%']
#['Ahmedabad '] [] ['Southeasterly 5.4km/h'] [' 46%']
#['Pune '] [] ['Southeasterly 25.9km/h'] [' 91%']
#['Delhi '] [] ['Northwesterly 9.3km/h'] [' 41%']




