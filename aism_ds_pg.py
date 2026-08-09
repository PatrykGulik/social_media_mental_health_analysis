import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/aism_ds_pg.csv')
### Dataset exploration
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

def scatter_plot(df, x_col, y_col, title, xlabel, ylabel):
    plt.scatter(x=df[x_col], y=df[y_col], s=5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

scatter_plot(df, 'Daily_Social_Media_Hours', 'Mental_Health_Score', 'Relationship between Mental Health and Social Media Usage', 'Daily Social Media Hours', 'Mental Health Score')
scatter_plot(df, 'Sleep_Hours', 'Mental_Health_Score', 'Relationship between Sleep and Mental Health', 'Daily Sleep Hours', 'Mental Health Score')
scatter_plot(df, 'Social_Isolation_Score', 'Mental_Health_Score', 'Relationship between Social Isolation and Mental Health', 'Social Isolation Score', 'Mental Health Score')
scatter_plot(df, 'Physical_Activity_Hours', 'Mental_Health_Score', 'Relationship between Physical Activity and Mental Health', 'Physical Activity Hours', 'Mental Health Score')
