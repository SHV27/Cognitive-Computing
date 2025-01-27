import numpy as np
import pandas as pd

dict1 = {
    "employee_id": [101, 102, 103, 104, 105],
    "name": ["alice", "bob", "charlie", "diana", "edward"],
    "department": ["hr", "it", "it", "marketing", "sales"],
    "age": [29, 34, 41, 28, 38],
    "salary": [50000, 70000, 65000, 55000, 60000],
    "years_of_experience": [4, 8, 10, 3, 12],
    "joining_date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "gender": ["female", "male", "male", "female", "male"],
    "bonus": [5000, 7000, 6000, 4500, 5000],
    "rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}
df = pd.DataFrame(dict1)
print(df)

print(df.shape)
print(df.info())
print(df.describe())
print(df.head(6))
print(df.tail(3))
print(df["salary"].mean())
print(df["bonus"].sum())
print(df["age"].min())
print(df["rating"].max())
print(df.sort_values(by="salary", ascending=False))

df["performance"] = pd.cut(df["rating"], bins=[0, 3.9, 4.4, 5], labels=["Average", "Good", "Excellent"])
print(df)

print(df.isnull().sum())

df.rename(columns={"employee_id": "id"}, inplace=True)
print(df)

print(df.loc[(df["years_of_experience"] > 5)])
print(df.loc[(df["department"] == "it")])

df["tax"] = df["salary"] * 0.1
print(df)

df.to_csv("modifiedd.csv")
