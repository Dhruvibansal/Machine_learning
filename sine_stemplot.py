import numpy as np
import matplotlib.pyplot as plt
from math import *
x= np.arange(-pi,pi,0.001)
x=list(x)
y=[]
for i in x:
   y.append(sin(i))


plt.stem(x,y)   
plt.show()
