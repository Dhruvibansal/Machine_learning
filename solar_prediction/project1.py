import pandas as pd
import matplotlib.pyplot as plt
cols=['Radiation','Temperature','TimeSunRise','TimeSunSet']
data=pd.read_csv('SolarPrediction1.csv')
x=data[cols]
##

import pandas as pd
import matplotlib.pyplot as plt

x=data[cols]
rad=data['Radiation']
temp=data['Temperature']
time=data['Time']

plt.subplot(131)
plt.scatter(time[:200],rad[:200],color='r')
plt.xlabel('Time')
plt.ylabel('Radiation')
plt.title('Time vs Radiation')


plt.subplot(132)
plt.scatter(time[:200],temp[:200],color='g')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Time vs Temperature')

#plt.show()

df=pd.read_csv('SolarPrediction1.csv')
uniq=["Data"]
df.drop_duplicates(subset=uniq,keep='first',inplace=True)

df.TimeSunRise=pd.to_datetime(df.TimeSunRise)
df.TimeSunSet=pd.to_datetime(df.TimeSunSet)
diff=df.TimeSunSet-df.TimeSunRise
diff=diff.reset_index()
newdiff=diff
print(diff[0])
newdiff[0].to_csv('SolarPrediction.csv')

plt.subplot(133)

plt.plot(newdiff[0])
plt.xlabel('Time')
plt.ylabel('Solar Hours')
plt.title('Time vs Solar Hours')
plt.show()
#print(df.data)
#lst=[df.Data,diff[0]]
#solar hours
