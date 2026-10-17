import pandas as pd
import numpy as np 
import seaborn as sd
import matplotlib.pyplot as mp

data=pd.read_csv(r"C:\Users\DEEPAK\Downloads\house_price_dirty_practice.csv")
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",100)
pd.set_option("display.float_format", "{:,.2f}".format)
#print(data.info(), data.shape)
#print(data["area_sqft"].head(50))
#print(data.loc[data["area_sqft"].isna(),"area_sqft"])

#converting sqft column from str to numeric value 
data["area_sqft"]=pd.to_numeric(data["area_sqft"].str.replace(",",""),errors="coerce")
data["sale_price_inr"]=pd.to_numeric(data["sale_price_inr"].str.replace(",",""),errors="coerce")
#print(data[["area_sqft","sale_price_inr"]].isna().sum())
#print(data["sale_price_inr"].head(100))
#print(data["location"].head(100))
#print(data.info())

#converting categorical data type into numerical
#step 1: standardize values
data["location"]=(data["location"]
                  .str.lower()
                  .str.strip()
                  .str.capitalize()
                  .fillna("unkown"))
#print(data["location"].unique()) 

#step 2 : one hot encoding 
from sklearn.preprocessing import OneHotEncoder
encoder=OneHotEncoder(handle_unknown="ignore",sparse_output=False)
#[["location"]] => no [location] it expects 2d 
encoded=encoder.fit_transform(data[["location"]])

#step 3 : converting numpy into dataframe
data_2=pd.DataFrame(encoded,columns=encoder.get_feature_names_out(["location"]),index=data.index)
#print(data_2)

#step 4: combining both columns 
data_3=pd.concat([data,data_2],axis=1)
#print(data_3)

data_3=data_3.drop(columns="location")
#print(data_3.isna().sum())
#print(data_3.describe())
data_3 = data_3.dropna(subset=["sale_price_inr"])
data_3.loc[:,"area_sqft":"location_unkown"]=data_3.loc[:,"area_sqft":"location_unkown"].fillna(data_3.loc[:,"area_sqft":"location_unkown"].median())
#print(data_3.isna().sum())

#finding correlation
#print(data_3.info())
#print(data_3.loc[:,"area_sqft":"location_unkown"].corr()["sale_price_inr"])

#plot sale_price_inr
s=sd.histplot(data_3["sale_price_inr"])
#mp.show()

#separate features and target data 
x=data_3.loc[:,["area_sqft","bedrooms","bathrooms","house_age_years","parking_spaces","location_Bengaluru","location_Chennai","location_Coimbatore","location_Madurai","location_Salem","location_Trichy","location_unkown"]]
y=data_3.loc[:,"sale_price_inr"]
#print(x)
#print((x<0).sum())

#replacing negative values which are present in x
cols=["area_sqft","bedrooms","parking_spaces"]
for col in cols:
    x.loc[x[col]<0,col]=np.nan
for col in cols:
    x[col]=x[col].fillna(x[col].median())

#printing x and y 
#print(x,y)

#splitting training and testing dataset 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=20)
#print(x_train.shape)
#print(x_test.shape)
#print(y_train.shape)
#print(y_test.shape)

#model training 
from sklearn.linear_model import LinearRegression
y_regression=LinearRegression()
y_regression.fit(x_train,y_train)
#print(y_regression.coef_,y_regression.intercept_)
#prediction
y_predict=y_regression.predict(x_test)
#print(y_predict)
#converting predicted 
y_pred=pd.DataFrame(y_predict,columns=["predict"])
#print(y_pred)
#newdataframe 
err_find=pd.DataFrame(columns=["actual","predicted","error"])
err_find["actual"]=y_test.reset_index()["sale_price_inr"]
err_find["predicted"]=y_pred.reset_index()["predict"]
err_find["error"]=err_find["actual"]-err_find["predicted"]
#print(err_find)

#metrics
from sklearn import metrics
mean_error=metrics.mean_absolute_error(y_test,y_pred)
print(mean_error)
from sklearn.metrics import r2_score
r2=r2_score(y_test,y_pred)
print(r2)

