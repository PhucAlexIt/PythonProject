import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('File_Analyst/chipotle.tsv', sep='\t')
df.item_price = df.item_price.apply(lambda x : float(x.replace('$','')))
df["total_price"] = df["quantity"] * df["item_price"]
# total = df["total_price"].sum()
# print(f' Total price: {total}')
# print(df.groupby("item_name").apply(print))
# c = df.groupby("item_name")["total_price"].sum()
# print(df.item_name.value_counts())
# print(df.item_name.value_counts().count())
print(df.item_name.nunique())
# print(c.sort_values(ascending=False).head(10))
# print(df.head(6))