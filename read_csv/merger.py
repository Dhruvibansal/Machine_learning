import pandas as pd
import numpy as np
df1=pd.read_csv('sample.csv')
df2=pd.read_csv('Vocab.csv')
lstimage=list(df1['Image_Name'])
lstvals=dict(df2['Values'])
changed_img=[]
for image_name in lstimage:
    new_image=image_name.split('-')
    searchval=int(new_image[2])
    if searchval in list(lstvals.keys()):
        new_image[2]=lstvals[searchval]
    img=''
    changed_img.append(img.join(new_image))

##print(changed_img)
##df=pd.DataFrame(changed_img)
##print(df)
##df1["Image_Name"]=df1["Image_Name"].map('{:,.2f}'.format)
##df1.to_csv('sample.csv')

##df1['​Image_Name'] = pd.where(df1['​Image_Name'] == 0, df['0'], df1['Image_Name'])

df1['Image_Name'] = df1['Image_Name'].replace(lstimage, changed_img)
df1.to_csv('sample.csv')
