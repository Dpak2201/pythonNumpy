import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import seaborn as se
#reading csv
data=pd.read_csv(r"C:\Users\DEEPAK\Downloads\heart-selected-columns.csv")
#print(data["target"].value_counts(normalize=True))
se.countplot(x="target",data=data)
#pl.show()
#dependent and independent variable mapping
x=pd.DataFrame(data.iloc[:,:-1])
y=pd.DataFrame(data.iloc[:,-1])
#print(x.head(),y.head())
#training and testing data 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.7,random_state=20)
#print(x_train.info())
#print(y_train.info())
#print(x_test.info())
#print(y_test.info())

#actual model training 
from sklearn.linear_model import LogisticRegression 
model_lg=LogisticRegression()
modell=model_lg.fit(x_train,y_train)
#print(modell)

#prediction 
prediction=model_lg.predict(x_test)
#print(prediction)
y_predict=pd.DataFrame(prediction,columns=["p"])
#print(y_predict)

#comparing predicted and actual [not required]
#comparison=pd.DataFrame(columns=["predicted","actual"])
#comparison["predicted"]=y_predict.reset_index()["p"]
#comparison["actual"]=y_test.reset_index()["target"]
#print(comparison.head(61))

#accuracy
accuracy_train=model_lg.score(x_train,y_train)
print("accuracy_train",accuracy_train)
accuracy_test=model_lg.score(x_test,y_test)
print("accuracy_test",accuracy_test)

#confusion_matrix
from sklearn.metrics import confusion_matrix
con_matrix=confusion_matrix(y_test,y_predict)
#print(con_matrix)
from sklearn.metrics import confusion_matrix
con_matrix=confusion_matrix(y_train,model_lg.predict(x_train))
#print(con_matrix)

from sklearn.metrics import classification_report
report=classification_report(y_test,y_predict)
print("report_test",report)
from sklearn.metrics import classification_report
report=classification_report(y_train,model_lg.predict(x_train))
print("report_train",report)
