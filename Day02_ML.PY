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
