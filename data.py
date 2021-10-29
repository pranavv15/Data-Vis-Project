from os import replace
import numpy as np
import pandas as pd


data = "United States and Puerto Rico Cancer Statistics, 1999-2017 Incidence Archive-2.csv"
df = pd.read_csv(data)
# print(df.head(5))
df = df.drop('Notes', axis=1)
df = df.drop(['Sex Code','States Code'], axis=1)
df = df.dropna()
rep = ["District of Columbia","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Rhode Island","South Carolina","South Dakota","West Virginia"]
val = ["District-of-Columbia","New-Hampshire","New-Jersey","New-Mexico","New-York","North-Carolina","North-Dakota","Rhode-Island","South-Carolina","South-Dakota","West-Virginia"]

df = df.replace(to_replace=rep, value=val)

df1 = df.pivot(index= "States", columns="Sex",values="Count")
df1.reset_index(inplace=True)

print(df.head(5))
# print(df1.head(20))
print(df1.head(20))

df1.to_csv("/Users/pranavvinod/Documents/GitHub/Data-Vis-Project/Cancer-Data.csv")