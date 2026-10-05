import matplotlib.pyplot as plt 
import pandas as pd 
#univariate 
data={"salary":[10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,200000,300000]}
df=pd.DataFrame(data)
#print(df)
#plt.plot(df["salary"],color="red",marker="*",linestyle="--",linewidth="2")
#plt.grid()
#plt.show()
#histogram 
#plt.hist(df["salary"],bins=5,color="green")
#plt.show()
#box plot
#plt.boxplot(df["salary"])
#plt.show()
#df.iloc[11]=[20]
#df.drop(index=11,inplace=True)
dept={"dept":["hr","fin","mark","ai","op","data","data","fin","op","ai","ai"]}
data1=pd.DataFrame(dept)
df=pd.concat([df,data1],axis=1)
#print(df)
#print(df)
#category based plot using pie 
count=df["dept"].value_counts()
#print(count)
#plt.pie(count,labels=count.index,autopct="%1.2f")
#plt.show()
#bar chart
#plt.bar(count.index,count)
#plt.show()
df["age"]=[25,26,27,28,29,30]*2
#print(df)
salary_sorted=df.sort_values("salary")
#print(salary_sorted)
#plt.scatter(salary_sorted["salary"],df["age"],color="red")
#plt.show()
salary_grp=df.groupby("dept")["salary"].sum()
#print(salary_grp)
#plt.pie(salary_grp,labels=salary_grp.index,autopct="%1.0f")
#plt.show()
#objectorientedapi
fig,axs=plt.subplots(1,3,figsize=(10,5))
fig.suptitle ="full dia"
axs[0].plot(salary_sorted["salary"],color="red",marker="*")
axs[0].set_xlabel="salary"
axs[1].hist(df["age"],bins=5)
axs[2].boxplot(df["salary"])
plt.show()