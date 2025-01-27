import numpy as np
import pandas as pd


data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "refund": ["yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no"],
    "marital status": ["single", "married", "single", "married", "divorced", "married", "divorced", "single", "married", "single"],
    "taxable income": ["125k", "100k", "70k", "120k", "95k", "60k", "220k", "85k", "75k", "90k"],
    "cheat": ["no", "no", "no", "no", "yes", "no", "no", "yes", "no", "yes"]
}


df = pd.DataFrame(data)


print(df)

# Question 2: Select specific rows
print(df.iloc[[0, 4, 7, 8]])

# Question 3.1: Slice rows 3 to 7
print(df.iloc[3:8])

# Question 3.2: Slice columns 2 to 4 for rows 4 to 8
print(df.iloc[4:9, 2:4])

# Question 3.3: Select all rows and columns 1 to 3
print(df.iloc[:, 1:4])
