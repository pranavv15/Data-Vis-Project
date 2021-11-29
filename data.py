from os import replace
import numpy as np
import pandas as pd

# Program to modify data

data = "data vis data/obesity_by_sex.csv"
df = pd.read_csv(data)
print(df.head(5))
# Dropping 3 columns and na values
df = df.drop('Footnotes', axis=1)
# df = df.drop(['Sex Code','States Code'], axis=1)
df = df.dropna()
print(df.head(5))


# Replacing spaces with "-"
rep = ["United States","District of Columbia","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Rhode Island","South Carolina","South Dakota","West Virginia"]
val = ["United-States","District-of-Columbia","New-Hampshire","New-Jersey","New-Mexico","New-York","North-Carolina","North-Dakota","Rhode-Island","South-Carolina","South-Dakota","West-Virginia"]
df = df.replace(to_replace=rep, value=val)

# Creating a table containing count of male and female cancer patients
# df1 = df.pivot(index= "Location", columns="Sex",values="Count")
# df1.reset_index(inplace=True)

# # Saving to another csv file
df.to_csv("/Users/pranavvinod/Documents/GitHub/Data-Vis-Project/Obesity-Data-Sex.csv")
print(df.head(5))
