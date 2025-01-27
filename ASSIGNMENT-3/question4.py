import numpy as np
import pandas as pd

df = pd.read_csv("Iris.csv")
print(df.head(5))

df = df.drop(index=3, axis=0)
df = df.drop('SepalWidthCm', axis=1)
print(df.head(5))
