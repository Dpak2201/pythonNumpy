import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
data=pd.read_csv(r"C:\Users\DEEPAK\Downloads\BostonHousing.csv")
pd.set_option("display.max_columns",None)
#print(data.describe().T)
#print(data.loc[:,"age"].median())
print(data.isna().sum())
data["rm"]=data["rm"].fillna(data["rm"].mean(),inplace=True)
sns.displot(data["age"])
#plt.hist(data["medv"])
#plt.show()
#print(data.corr()["medv"])
#data preparation 
x=pd.DataFrame(data.loc[:,("lstat","rm","dis","b")])#independent variable 
y=pd.DataFrame(data["medv"])#dependent variable 
print(x,y)
#splitting training and testing data 
import sklearn as sk
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=20)
#print(x_train,x_test,y_train,y_test)
#print(x_train.shape)
#print(x_test.shape)
#print(y_train.shape)
#print(y_test.shape)
#select model and fit it 
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(x_train,y_train)
##print(regression.coef_)
#print(regression.intercept_)
#model testing 
y_predict=regression.predict(x_test)
#print(y_predict)
data_1=pd.DataFrame(y_predict,columns=["predicted"])
df=pd.DataFrame(columns=["pred","actual","error"])
df["pred"]=data_1.reset_index()["predicted"]
df["actual"]=y_test.reset_index()["medv"]
df["error"]=df[("actual")]-df[("pred")]
#print(df)
from sklearn import metrics
error=metrics.mean_absolute_error(data_1,y_test)
sq=metrics.mean_squared_error(data_1,y_test)
rt=metrics.root_mean_squared_error(data_1,y_test)
#print(error,sq,rt)
from sklearn.metrics import r2_score
rscore=r2_score(data_1,y_test)
print(rscore)