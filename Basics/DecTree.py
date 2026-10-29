import pandas as pd
import numpy as np 

#reading data 
data=pd.read_csv(r"C:\Users\DEEPAK\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")
data["TotalCharges"]=pd.to_numeric(data["TotalCharges"],errors="coerce")
data["TotalCharges"].dropna(inplace=True)
data=data.drop(columns=["customerID"])
from sklearn.preprocessing import LabelEncoder
encoder =LabelEncoder()
cols=['gender','Partner', 'Dependents',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
       'MonthlyCharges', 'TotalCharges', 'Churn']
for c in cols:
    if data[c].dtype=="str":
      data[c]=encoder.fit_transform(data[c])

#print(data.info())

#diving features and target
x=data.iloc[:,:-1]
y=data.iloc[:,-1]

#splitting training and testing data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,random_state=25)
#print(x_train.shape)
#print(y_train.shape)
#print(x_test.shape)
#print(y_test.shape)

#decision tree
from sklearn.tree import DecisionTreeClassifier
t=DecisionTreeClassifier()
op=t.fit(x_train,y_train)
pred=t.predict(x_test)
pred_train=t.predict(x_train)

#accuracy score
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,roc_auc_score)
#print("testingaccuracy",accuracy_score(y_test,pred))
#print("trainingaccuracy",accuracy_score(y_train,pred_train))




#hyper paramater tuning for random forest 

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
n_estimators=[int(x) for x in np.linspace(100,500,10)]
#print(n_estimators)
criterion=["gini","entropy"]
max_features=["sqrt"]
bootstrap =[True,False]
max_depth = [int(x) for x in np.linspace(2,10,6)]
#print(max_depth)
min_samples_split=[int(x) for x in np.linspace(10,20,10)]
min_samples_leaf=[int(x) for x in np.linspace(10,20,10)]

random_grid={"n_estimators":n_estimators,
             "criterion":criterion,
             "min_samples_leaf":min_samples_leaf,
             "bootstrap":bootstrap,
             "max_depth":max_depth,
             "min_samples_split":min_samples_split,
             "max_features":max_features}
#print(random_grid)

from sklearn.model_selection import RandomizedSearchCV
model=RandomizedSearchCV(estimator=rf,param_distributions=random_grid,n_iter=20,n_jobs=-1,verbose=2,cv=5,random_state=42,return_train_score=True,scoring="accuracy")
random_model=model.fit(x_train,y_train)
#print(random_model.best_params_)
#print(random_model.best_score_)
#print(random_model.best_estimator_)
best_model=random_model.best_estimator_
pre_rf=best_model.predict(x_test)
pre_rf_train=model.predict(x_train)
print("accuracyscore_train",accuracy_score(pre_rf_train,y_train))
print(accuracy_score(pre_rf,y_test)) 
print(classification_report(pre_rf_train,y_train))
print(classification_report(pre_rf,y_test))
