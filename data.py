from os import replace
import numpy as np
import pandas as pd

# Program to modify data

data = "data vis data/obesity_by_sex.csv"
data1 = "data vis data/Asthma_by_sex.csv"
data2 = "data vis data/Heart_by_sex.csv"
data3 = "data vis data/Diabetes_by_sex.csv"

df = pd.read_csv(data)
df1 = pd.read_csv(data1)
df2 = pd.read_csv(data2)
df3 = pd.read_csv(data3)

# print(df2.head(5))
# Dropping 3 columns and na values
df = df.drop('Footnotes', axis=1)
df1 = df1.drop(['Footnotes','Location'], axis=1)
df2 = df2.drop(['Footnotes','Location'], axis=1)
df3 = df3.drop(['Footnotes','Location'], axis=1)

# df = df.drop(['Sex Code','States Code'], axis=1)
df = df.dropna()
df1 = df1.dropna()
df2 = df2.dropna()
df3 = df3.dropna()
print(df3.head(5))


# Replacing spaces with "-"
rep = ["United States","District of Columbia","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Rhode Island","South Carolina","South Dakota","West Virginia"]
val = ["United-States","District-of-Columbia","New-Hampshire","New-Jersey","New-Mexico","New-York","North-Carolina","North-Dakota","Rhode-Island","South-Carolina","South-Dakota","West-Virginia"]
df = df.replace(to_replace=rep, value=val)


# Creating a table containing count of male and female cancer patients
# df1 = df.pivot(index= "Location", columns="Sex",values="Count")
# df1.reset_index(inplace=True)

# # Saving to another csv file
# df.to_csv("/Users/pranavvinod/Documents/GitHub/Data-Vis-Project/Obesity-Data-Sex.csv")
# print(df.head(5))
