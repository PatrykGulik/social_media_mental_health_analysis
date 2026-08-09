import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

df = pd.read_csv('data/aism_ds_pg.csv')

### Dataset exploration
def explore_dataset(df):
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

### Data Visualization
def scatter_plot(df, x_col, y_col, title, xlabel, ylabel):
    plt.scatter(x=df[x_col], y=df[y_col], s=5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

#scatter_plot(df, 'Daily_Social_Media_Hours', 'Mental_Health_Score', 'Relationship between Mental Health and Social Media Usage', 'Daily Social Media Hours', 'Mental Health Score')
#scatter_plot(df, 'Sleep_Hours', 'Mental_Health_Score', 'Relationship between Sleep and Mental Health', 'Daily Sleep Hours', 'Mental Health Score')
#scatter_plot(df, 'Social_Isolation_Score', 'Mental_Health_Score', 'Relationship between Social Isolation and Mental Health', 'Social Isolation Score', 'Mental Health Score')
#scatter_plot(df, 'Physical_Activity_Hours', 'Mental_Health_Score', 'Relationship between Physical Activity and Mental Health', 'Physical Activity Hours', 'Mental Health Score')

#### Correlation Analysis

def correlation_analysis(df):
    social_media_corr = df['Daily_Social_Media_Hours'].corr(df['Mental_Health_Score'])
    sleep_corr = df['Sleep_Hours'].corr(df['Mental_Health_Score'])
    social_isolation_corr = df['Social_Isolation_Score'].corr(df['Mental_Health_Score'])
    physical_activity_corr = df['Physical_Activity_Hours'].corr(df['Mental_Health_Score'])
    print(f"Correlation between Daily Social Media Hours and Mental Health Score: {social_media_corr}")
    print(f"Correlation between Sleep Hours and Mental Health Score: {sleep_corr}")
    print(f"Correlation between Social Isolation Score and Mental Health Score: {social_isolation_corr}")
    print(f"Correlation between Physical Activity Hours and Mental Health Score: {physical_activity_corr}")

correlation_analysis(df)

correlation, p_value = pearsonr(df['Daily_Social_Media_Hours'], df['Mental_Health_Score'])
print(f"Correlation: {correlation}")
print(f"P-value: {p_value:.20e}")
