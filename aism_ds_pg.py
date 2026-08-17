import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, linregress
import statsmodels.api as sm
import statsmodels.stats.api as sms

# Functions

def explore_dataset(df):
    return {"head": df.head(), 
            "description": df.describe(), 
            "null_counts": df.isnull().sum(), 
            "duplicate_counts": df.duplicated().sum()} 


def explore_categorical_columns(df):
    categorical_columns = df.select_dtypes(include=['str', 'object'])
    gender_counts = df['Gender'].value_counts()
    education_count = df['Education_Level'].value_counts()
    burnout_count = df['Burnout_Level'].value_counts()
    return categorical_columns, gender_counts, education_count, burnout_count


def plot_histogram(df, column, title, xlabel, ylabel):
    plt.hist(df[column], bins=20, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def scatter_plot(df, x_col, y_col, title, xlabel, ylabel):
    plt.scatter(x=df[x_col], y=df[y_col], s=5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


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


def calculate_mean_mental_health(high_group, low_group):
    mean_mental_health_high = high_group['Mental_Health_Score'].mean()
    mean_mental_health_low = low_group['Mental_Health_Score'].mean()
    return mean_mental_health_high, mean_mental_health_low


def calculate_mental_health_std(high_group, low_group):
    std_high = high_group['Mental_Health_Score'].std()
    std_low = low_group['Mental_Health_Score'].std()
    return std_high, std_low


def cohens_d(high_group, low_group):
    mean_mental_health_high = high_group['Mental_Health_Score'].mean()
    mean_mental_health_low = low_group['Mental_Health_Score'].mean()
    pooled_std = np.sqrt((high_group['Mental_Health_Score'].var() + low_group['Mental_Health_Score'].var()) / 2)
    cohens_d_value = (mean_mental_health_high - mean_mental_health_low) / pooled_std
    return cohens_d_value


def linear_regression(df, x_col, y_col):
    result = linregress(df[x_col], df[y_col])
    return result

def multiple_linear_regression(df, x_cols, y_col):
    X = df[x_cols]
    y = df[y_col]
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()

    predictions = results.predict(X)
    residuals = y - predictions

    breusch_pagan_test = sms.het_breuschpagan(residuals, X)

    robust_model = results.get_robustcov_results(cov_type='HC3')

    return results, predictions, residuals, breusch_pagan_test, robust_model


# Load the dataset

df = pd.read_csv('data/AI_SocialMedia_Student_Health_Dataset_clean.csv')


# Analysis 

dataset_exploration = explore_dataset(df)

categorical_columns, gender_counts, education_count, burnout_count = explore_categorical_columns(df)

social_media_corr, sleep_corr, social_isolation_corr, physical_activity_corr = correlation_analysis(df)

correlation, p_value = pearsons_correlation(df, 'Daily_Social_Media_Hours', 'Mental_Health_Score')

high_users, low_users = split_social_media_groups(df)

mean_mental_health_high, mean_mental_health_low = calculate_mean_mental_health(high_users, low_users)

std_high, std_low = calculate_mental_health_std(high_users, low_users)

cohens_d_value = cohens_d(high_users, low_users)

linear_regression_result = linear_regression(df, 'Daily_Social_Media_Hours', 'Mental_Health_Score')

multiple_linear_regression_result, multiple_linear_regression_predictions, multiple_linear_regression_residuals, breusch_pagan_test, robust_model = multiple_linear_regression(df, ['Daily_Social_Media_Hours', 'Sleep_Hours', 'Social_Isolation_Score', 'Physical_Activity_Hours'], 'Mental_Health_Score')


#Results

print("Dataset Exploration:")
for key, value in dataset_exploration.items():
    print(f"{key.capitalize()}:")
    print(value)

print("Categorical Columns Exploration:")
print(f"Categorical Columns: {categorical_columns.shape[0]}")
print(f"Gender Counts:\n{gender_counts}")
print(f"Education Level Counts:\n{education_count}")
print(f"Burnout Level Counts:\n{burnout_count}")

# Correlation Analysis
print(f"Correlation between Daily Social Media Hours and Mental Health Score: {social_media_corr:.3f}")
print(f"Correlation between Sleep Hours and Mental Health Score: {sleep_corr:.3f}")
print(f"Correlation between Social Isolation Score and Mental Health Score: {social_isolation_corr:.3f}")
print(f"Correlation between Physical Activity Hours and Mental Health Score: {physical_activity_corr:.3f}")

# Pearson's Correlation
print(f"Correlation: {correlation:.2f}")
print(f"P-value: {p_value:.20e}")

# Split Social Media Groups
print(f"High social media group size: {len(high_users)}")
print(f"Low social media group size: {len(low_users)}")

# Mean Mental Health Scores
print(f"Mean mental health score for high social media users: {mean_mental_health_high:.3f}")
print(f"Mean mental health score for low social media users: {mean_mental_health_low:.3f}")

# Standard Deviation of Mental Health Scores
print(f"High social media SD: {std_high:.3f}")
print(f"Low social media SD: {std_low:.3f}")

# Cohen's d
print(f"Cohen's d: {cohens_d_value:.3f}")

# Linear Regression
print(
    f"Linear Regression Result: slope={linear_regression_result.slope:.3f}", 
    f"intercept={linear_regression_result.intercept:.3f}", 
    f"rvalue={linear_regression_result.rvalue:.3f}", 
    f"pvalue={linear_regression_result.pvalue:.3e}", 
    f"stderr={linear_regression_result.stderr:.3f}",
    f"intercept_stderr={linear_regression_result.intercept_stderr:.3f}"
)

# Multiple Linear Regression
print("Multiple Linear Regression Result:")
print(multiple_linear_regression_result.summary())

# Multiple Linear Regression Residuals
print("Multiple Linear Regression Residuals:")
print(multiple_linear_regression_residuals.head())

# Breusch-Pagan Test
print("Breusch-Pagan Test Result:")
print(f"LM Statistic: {breusch_pagan_test[0]:.3f}")
print(f"LM p-value: {breusch_pagan_test[1]:.3f}")   

# Robust Model Summary
print("Robust Model Summary:")
print(robust_model.summary())

# Data Visualization
show_histograms = True
if show_histograms:
    plot_histogram(df, 'Mental_Health_Score', 'Distribution of Mental Health Scores', 'Mental Health Score', 'Frequency')
    plot_histogram(df, 'Daily_Social_Media_Hours', 'Distribution of Daily Social Media Hours', 'Daily Social Media Hours', 'Frequency')


show_plots = True
if show_plots:
    scatter_plot(df, 'Daily_Social_Media_Hours', 'Mental_Health_Score', 'Relationship between Mental Health and Social Media Usage', 'Daily Social Media Hours', 'Mental Health Score')
    scatter_plot(df, 'Sleep_Hours', 'Mental_Health_Score', 'Relationship between Sleep and Mental Health', 'Daily Sleep Hours', 'Mental Health Score')
    scatter_plot(df, 'Social_Isolation_Score', 'Mental_Health_Score', 'Relationship between Social Isolation and Mental Health', 'Social Isolation Score', 'Mental Health Score')
    scatter_plot(df, 'Physical_Activity_Hours', 'Mental_Health_Score', 'Relationship between Physical Activity and Mental Health', 'Physical Activity Hours', 'Mental Health Score')


show_residual_plots = True
if show_residual_plots:
    plt.scatter(multiple_linear_regression_predictions, multiple_linear_regression_residuals, s=5)
    plt.axhline(y=0, color='black', linestyle='--')

    plt.xlabel('Predicted Mental Health Score')
    plt.ylabel('Residuals')
    plt.title('Residuals vs Predicted Mental Health Score')

    plt.show()

show_qq_plot = True
if show_qq_plot:
    sm.qqplot(multiple_linear_regression_residuals, line='s')
    plt.title('Q-Q Plot of Residuals')
    plt.show()

show_residual_histogram = True
if show_residual_histogram:
    plot_histogram(pd.DataFrame(multiple_linear_regression_residuals, columns=['Residuals']), 'Residuals', 'Distribution of Residuals', 'Residuals', 'Frequency')
