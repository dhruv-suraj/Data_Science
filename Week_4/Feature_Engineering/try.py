import pandas as pd
import numpy as np

df=pd.read_csv('train.csv')
# print(df.head())  #print first five values
# print(df.isnull().sum())  #To find sum of missing values in a dataset
# print(df[df['Embarked'].isnull()])
df['cabin_null']=np.where(df["Cabin"].isnull(),1,0) #1 is for missing and o for not missing data that means 0 is for not survived
print(df['cabin_null'].mean())  #percentage of null value
# print(df.columns)
print(df.groupby(["Survived"])['cabin_null'].mean())