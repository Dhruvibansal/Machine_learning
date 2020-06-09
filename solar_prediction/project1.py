import pandas as pd
import matplotlib.pyplot as plt
cols=['Radiation','Temperature','TimeSunRise','TimeSunSet']
data=pd.read_csv('SolarPrediction1.csv')
x=data[cols]

#print(date:solarhours)

#print(x)
import pandas as pd
import matplotlib.pyplot as plt

x=data[cols]
rad=data['Radiation']
temp=data['Temperature']
time=data['Time']

plt.scatter(time[:200],rad[:200],color='r')
plt.scatter(time[:200],temp[:200],color='g')

plt.show()

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

plt.subplot(131)
plt.subplot(132)
plt.subplot(133)
plt.plot(newdiff[0])
plt.show()
#print(df.data)
#lst=[df.Data,diff[0]]
#solar hours
