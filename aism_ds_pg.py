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

# Functions for Analysis

def correlation_analysis(df):
    social_media_corr = df['Daily_Social_Media_Hours'].corr(df['Mental_Health_Score'])
    sleep_corr = df['Sleep_Hours'].corr(df['Mental_Health_Score'])
    social_isolation_corr = df['Social_Isolation_Score'].corr(df['Mental_Health_Score'])
    physical_activity_corr = df['Physical_Activity_Hours'].corr(df['Mental_Health_Score'])
    return social_media_corr, sleep_corr, social_isolation_corr, physical_activity_corr


def pearsons_correlation(df, col1, col2):
    correlation, p_value = pearsonr(df[col1], df[col2])
    return correlation, p_value

def split_social_media_groups(df):
    mean_social_media  = df['Daily_Social_Media_Hours'].mean()

    high_users  = df[df['Daily_Social_Media_Hours'] > mean_social_media]
    low_users  = df[df['Daily_Social_Media_Hours'] <= mean_social_media]
    
    return high_users, low_users 

def mean_social_media_hours(df):
    mean_high = high_users['Mental_Health_Score'].mean()
    mean_low = low_users['Mental_Health_Score'].mean()

    return mean_high, mean_low

def calculate_mental_health_std(high_group, low_group):
    std_high = high_group['Mental_Health_Score'].std()
    std_low = low_group['Mental_Health_Score'].std()

    return std_high, std_low

def cohens_d(high_group, low_group):
    mean_high = high_group['Mental_Health_Score'].mean()
    mean_low = low_group['Mental_Health_Score'].mean()
    pooled_std = np.sqrt((high_group['Mental_Health_Score'].var() + low_group['Mental_Health_Score'].var()) / 2)
    d = (mean_high - mean_low) / pooled_std
    return d

# Analysis 

social_media_corr, sleep_corr, social_isolation_corr, physical_activity_corr = correlation_analysis(df)
correlation, p_value = pearsons_correlation(df, 'Daily_Social_Media_Hours', 'Mental_Health_Score')
high_users, low_users = split_social_media_groups(df)
mean_high, mean_low = mean_social_media_hours(df)
std_high, std_low = calculate_mental_health_std(high_users, low_users)
cohens_d(high_users, low_users)


#Results

# Correlation Analysis
print(f"Correlation between Daily Social Media Hours and Mental Health Score: {social_media_corr}")
print(f"Correlation between Sleep Hours and Mental Health Score: {sleep_corr}")
print(f"Correlation between Social Isolation Score and Mental Health Score: {social_isolation_corr}")
print(f"Correlation between Physical Activity Hours and Mental Health Score: {physical_activity_corr}")

# Pearson's Correlation
print(f"Correlation: {correlation}")
print(f"P-value: {p_value:.20e}")

# Mean Mental Health Scores
print(f"Mean mental health score for high social media users: {mean_high}")
print(f"Mean mental health score for low social media users: {mean_low}")

# Standard Deviation of Mental Health Scores
print(f"High social media SD: {std_high}")
print(f"Low social media SD: {std_low}")
