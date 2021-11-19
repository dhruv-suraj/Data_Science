import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# df=pd.read_csv('train.csv')
# # print(df.head())  #print first five values
# # print(df.isnull().sum())  #To find sum of missing values in a dataset
# # print(df[df['Embarked'].isnull()])
# df['cabin_null']=np.where(df["Cabin"].isnull(),1,0) #1 is for missing and o for not missing data that means 0 is for not survived
# print(df['cabin_null'].mean())  #percentage of null value
# # print(df.columns)
# print(df.groupby(["Survived"])['cabin_null'].mean())


# Mean/Median/Mode replacement:-

df=pd.read_csv('train.csv',usecols=['Age','Fare','Survived'])
print(df.head())
print(df.isnull().mean())

def impute_nan(df,variable,median):
    df[variable+"_median"]=df[variable].fillna(median)
median=df.Age.median()
print(median)
impute_nan(df,'Age',median) #hence all missing values will be filled by median
print(df.head())
print(df["Age"].std())
print(df["Age_median"].std())
fig = plt.figure()
ax = fig.add_subplot(111)
df['Age'].plot(kind='kde', ax=ax)
df.Age_median.plot(kind='kde', ax=ax, color='red')
lines, labels = ax.get_legend_handles_labels()
ax.legend(lines,labels,loc="best")