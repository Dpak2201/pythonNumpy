import pandas as pd
import numpy as np 
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",100)
#importing file 
data=pd.read_csv(r"C:\Users\DEEPAK\Downloads\heart-selected-columns-messy-word-labels.csv")
#print(f"datahead ={data.head()}")

#convert object to float
data["age"]=pd.to_numeric(data["age"],errors="coerce")
#print(data["age"].isna().sum())
for index,row in data["age"].items():
  if (row>=100) or (row<=0):
    #print("index",index,"age",row)
    data["age"]=data["age"].drop(axis=0,index=[154,259])
#print(data.isna().sum())
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
col=["sex","cp","fbs","restecg","exang","slope","target"]
for column in col:
   data[column]=encoder.fit_transform(data[column].astype(str))
#print(data.info())
print(data.isna().sum())