import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/aism_ds_pg.csv')

print(df.head())
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


categorical_columns = df.select_dtypes(include=['str', 'object'])
print(categorical_columns)
print(categorical_columns.describe())

gender_counts = df['Gender'].value_counts()
print(gender_counts)

education_count = df['Education_Level'].value_counts()
print(education_count)

burnout_count = df['Burnout_Level'].value_counts()
print(burnout_count)