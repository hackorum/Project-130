import pandas as pd
import csv

df = pd.read_csv("data.csv")

del df["num"]
del df["no"]
del df["Luminosity"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Star_name.1"]
df.to_csv("cleaned_data.csv")
del df["Unnamed: 6"]
df.to_csv("cleaned_data.csv")
