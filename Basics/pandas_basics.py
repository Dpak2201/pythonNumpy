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
print(df,
      df.head(1),
      df.tail(1),
      df.info())
