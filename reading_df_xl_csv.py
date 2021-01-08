import xlsxwriter
import csv
import pandas,os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('_file_')))
image_dir=os.path.join(BASE_DIR,'/content/drive/MyDrive/share_public/Unzipped/user3')
os.chdir(image_dir)
df=pandas.read_excel('copyuser3.xlsx')
af=df["Image_name"]
df1=pandas.read_csv('/content/drive/MyDrive/share_public/Unzipped/user3/vocab.csv' ,names=['Values'])
print(af)
print(df1)
