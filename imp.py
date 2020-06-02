#import numpy
#import matplotlib
#import pandas
x=[1,30,45,60,90,105,120,135,150,165,180]
y=[]
from math import*
for i in x:
	y.append(sin(i))

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

