import pandas as pd

df = pd.read_csv("BMW sales data (2010-2024) (1).csv")


df.shape
df.dtypes
df.isnull().sum()

df["Mileage_KM"] = df["Mileage_KM"].astype(float)

df = pd.get_dummies(df, drop_first=True)
print(df.head())

import seaborn as sns
import matplotlib.pylab as plt

sns.boxplot(x=df["Sales_Volume"])
plt.show()