##START OF ML


>> import numpy as np
>>> np.array([1,2,3])
array([1, 2, 3])
>>> arr=np.array([1,2,3,4])
>>> arr.ndim
1

>>> arr.ndim
1
                             ^
S
>>> arr=np.array([[1,2,3],[4,5,6],[7,7,8]])
>>> arr.ndim
2
>>> data=np.array([[1,2,3,4,5,6],[6,5,4,3,2,1]])
>>> 
>>> arr.ndim
2
>>> arr
array([[1, 2, 3],
       [4, 5, 6],
       [7, 7, 8]])
>>> import matplotlib.pyplot as pl
>>> pl.plot(data[0],data[1])
[<matplotlib.lines.Line2D object at 0x7fe1fbfce518>]
>>> pl.show()
>>> ar=np.array([45])
>>> ar.ndim
1
>>> ar=np.array(45)
>>> ar.ndim
0
>>> arr=np.array([1.1,2.2,3.3,4.4])
>>> newarr=arr.astype(str)
>>> newarr
array(['1.1', '2.2', '3.3', '4.4'], dtype='<U32')
>>> newarr.dtype
dtype('<U32')
>>> newarr=arr.astype(int)
>>> newarr.dtype
dtype('int64')

arr.shape
(4,)
>>> data=np.array([[1,2,3,4,5,6],[6,5,4,3,2,1]])
>>> data.shape
(2, 6)
>>> data.reshape(6,2)
array([[1, 2],
       [3, 4],
       [5, 6],
       [6, 5],
       [4, 3],
       [2, 1]])
data.flatten()
array([1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1])
>>> data.reshape(6,2)
array([[1, 2],
       [3, 4],
       [5, 6],
       [6, 5],
       [4, 3],
       [2, 1]])
>>> data.ravel()
array([1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1])
#ravel and flatten same

 for i in data :
...     print(i)
... 
[1 2 3 4 5 6]
[6 5 4 3 2 1]

# ARROW PLOT AND STEM PLOT
 x=[1,2,3]
>>> y=[4,5,6]
>>> plt.Arrow(5,5,1,1)
<matplotlib.patches.Arrow object at 0x7fe208031240>
>>> plt.show()
>>> plt.stem(x,y)
__main__:1: UserWarning: In Matplotlib 3.3 individual lines on a stem plot will be added as a LineCollection instead of individual lines. This significantly improves the performance of a stem plot. To remove this warning and switch to the new behaviour, set the "use_line_collection" keyword argument to True.
<StemContainer object of 3 artists>
>>> plt.show()

 plt.bar(x,y)
<BarContainer object of 3 artists>
>>> plt.show()

#PIE PLOT
 y=[20,30,40,50,80,78]
>>> plt.pie(y)
([<matplotlib.patches.Wedge object at 0x7fe1f33ec8d0>, <matplotlib.patches.Wedge object at 0x7fe1f33ece10>, <matplotlib.patches.Wedge object at 0x7fe1f33fa358>, <matplotlib.patches.Wedge object at 0x7fe1f33fa860>, <matplotlib.patches.Wedge object at 0x7fe1f33fad68>, <matplotlib.patches.Wedge object at 0x7fe1f34062b0>], [Text(1.0756398265032592, 0.23021503782341984, ''), Text(0.8138283050794426, 0.7400564099117863, ''), Text(0.10421183663359666, 1.0950524613485204, ''), Text(-0.8292499872772425, 0.7227340164961751, ''), Text(-0.873276624442352, -0.6688706431011691, ''), Text(0.7485947317945707, -0.805981344405325, '')])
>>> plt.show
<function show at 0x7fe2149b87b8>
>>> plt.show()

plt.bar(student,marks)

import pandas
>>> import pandas as pd
>>> pd.read_csv
<function _make_parser_function.<locals>.parser_f at 0x7fe1db57d6a8>
>>> data=pd.read_csv('abc.csv')
>>> data
   1 smart phone   50
0  2          tv  100
1  3         usb  300
2  4     charger   50

