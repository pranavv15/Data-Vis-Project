import numpy as np
import pandas as pd


data = "United States and Puerto Rico Cancer Statistics, 1999-2017 Incidence Archive-2.csv"
df = pd.read_csv(data)
# print(df.head(5))
df = df.drop('Notes', axis=1)
df = df.drop(['Sex Code','States Code'], axis=1)
df = df.dropna()
df1 = df.pivot(index= "States", columns="Sex",values="Count")
print(df.head())
print(df1.head(20))
df1.to_csv("/Users/pranavvinod/Documents/GitHub/Data-Vis-Project/Cancer-Data.csv")