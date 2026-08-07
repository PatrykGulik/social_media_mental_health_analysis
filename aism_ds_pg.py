import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/aism_ds_pg.csv')

print(df.head)
print()

print(df.describe())
print()

print(df.info())
print()

print("Missing values in each column:")
print(df.isnull().sum())
print()

print(f"Duplicate rows: {df.duplicated().sum()}")
print()