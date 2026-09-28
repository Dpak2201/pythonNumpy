import pandas as pd
import numpy as np
#creating a series(series= one dimensional(one column),homogeneous,size imumtable, if you change the size new series will be formed )
se=pd.Series((1000,2000,3000),index=["house1","house2","house3"],name="sq.ft")
#se.name="sq.ft"
#print(f'length={len(se)},series={se}')
#ind=["house1","house2","house3","house4"]
#se.index= ind
#print(se["house1"])
#loc and iloc
#loc=labelled based indexing (very important will include the stop value also)
#iloc=index based indexing(will not include stop value)
#print(se.loc["house1":"house4"])
#print(se.iloc[0:3])
#series using dic 
di={"apple":0.20,"orange":0.30,"banana":0.40,"grapes":0.10}
s2=pd.Series(di,name="protein in grams")
#print(s2)
#conditional statements
#print(s2[s2>0.20])
#logical operators (in python and,or , not , in pandas =&,|,~)
#print(s2[(s2>=0.20)&(s2<=0.40)])
#print(s2[(s2>=0.20)|(s2<=0.40)])
#print(s2[~(s2==0.40)])
#not null 
sp=pd.Series([1,np.nan,2,np.nan],index=["a","b","c","d"],name="testing")
#print(sum(sp.notnull()),np.isnan(sp),pd.isna(sp))
data={"name":["Deepak","Kags","Poornima","dharani","x","y"],
      "age":[28,28,31,32,pd.NA,pd.NA],
      "city":["blr","chn","cbe","singa",pd.NA,pd.NA]}
df=pd.DataFrame(data)
#print(df,df.head(1),df.tail(1),df.info())
#print(df.iloc[0:3,[0,1]])
#print(df[["age","city"]])
#print(df.drop("city",axis=1))
#print(df.drop(columns=["age","city"]))
#print(df.shape)
#df.info
#print(df.info()) #deifference bewteen info and info(), () is always execution , info will give attribute alone
#broadcasting
df["age"]+= 5
#print(df)
#rename
#print(df.rename(columns={"city":"place"},inplace=True))
#print(df)
#print(df["age"].value_counts())
#data cleaning
#getting rid of null values 
#print(df.isnull().sum())
#print(df.dropna(how="all"))
#filling instead of dropping 
#filling using a random value
#print(df.fillna(value=0))
#filling using mean , median , mode for numerical values 
#print(df["age"].fillna(df["age"].mean()).astype(int))
#filling NA for string , using a value or mode 
#print(df["city"].fillna(df["city"].mode()[0]))
#print(df["city"].fillna(value="chennai"))
#forward fill and backward fill 
#print(df.ffill())
#print(df.bfill())
#addition of row 
#df.loc[len(df)]=["Deepak",28,"dpi"]
#df.loc[len(df)]={"name":"Dpak","age":27,"city":"dhar"}
#print(df)
#addition of multiple rows
new_one={"name":["sam","sanjeev","praba","jessil"],"age":[28,28,27,28],"city":["ney","chn","blr","usa"]}
new_ones=pd.DataFrame(new_one)
df=pd.concat([df,new_ones],ignore_index=True)
#print(df)
#print(df[df.isna().any(axis=1)])
#print(df[df[["age","city"]].duplicated(keep="first")])
#print(df["age"].apply(lambda x:x+5))
#import csv
data=pd.read_csv(r"C:\Users\DEEPAK\Downloads\archive (4)\House Price Prediction Dataset.csv")
#print(data.head())
print(data.info())