# Social Media Impact on Mental Health

An exploratory data science and statistical analysis project investigating the relationship between **daily social media use** and **mental health** among students.

The project uses a synthetic student health and academic performance dataset to explore whether patterns of social media usage are associated with mental health scores, while also considering other behavioural factors such as sleep, physical activity, and social isolation.

> **Note:** This project is primarily an educational data science project focused on statistical analysis and interpretation. The dataset is synthetic, and the results should not be interpreted as evidence of causal relationships in real student populations.

## Learning Objectives

This project was developed as a practical exercise in applying statistical and data science techniques to a complete analytical question.

The project provided experience with:

* Data cleaning and validation
* Exploratory data analysis
* Statistical visualisation
* Pearson correlation
* Hypothesis testing
* Effect-size interpretation
* Simple linear regression
* Multiple linear regression
* Regression diagnostics
* Heteroscedasticity
* Robust standard errors
* Statistical interpretation
* Communicating analytical findings

## Research Question

**Is
higher daily social-media use associated with lower mental health scores?**

The analysis investigates this question using exploratory data analysis, correlation analysis, hypothesis testing, effect-size analysis, and linear regression.

### Hypotheses

**H₀ (Null Hypothesis):**
There is no linear relationship between social-media usage and mental-health
score

**H₁ (Alternative Hypothesis):**
There is a negative linear association
between daily social media usage and mental health scores

## Dataset

The project uses the **AI & Social Media Impact: Student Health & Grades** dataset.

The dataset contains **15,000 observations**, designed as a synthetic, machine-learning-ready dataset and includes the following variables:

* Daily social media usage
* AI tool usage
* Sleep duration
* Physical activity
* Mental health score
* Social isolation score
* Academic performance
* Burnout indicators
* Demographic characteristics

Initial data-quality checks found:

* No missing values
* No duplicate observations
* Numerical and categorical variables suitable for exploratory and statistical analysis

## Analysis

The project follows a progression from exploratory analysis to statistical modelling.

### 1. Exploratory Data Analysis

The dataset was initially examined using descriptive statistics and visualisations to understand:

* Variable distributions
* Central tendency and variation
* Potential relationships between variables
* Possible outliers and unusual observations

Particular attention was given to the relationship between:

**Daily Social Media Hours → Mental Health Score**

### 2. Correlation Analysis

Pearson correlation was used to measure the strength and direction of linear relationships between mental health score and selected behavioural variables.

Key correlations included:

| Variable                 | Correlation with Mental Health Score |
| ------------------------ | -----------------------------------: |
| Daily Social Media Hours |                           **-0.400** |
| Sleep Hours              |                           **+0.311** |
| Social Isolation Score   |                           **-0.292** |
| Physical Activity Hours  |                           **+0.246** |

The strongest observed relationship was the negative association between daily social media use and mental health score.

### 3. Hypothesis Testing

A Pearson correlation test was conducted for daily social media hours and mental health score, which provieded strong statistical evidence against the null hypothesis of no linear association within this dataset.

The analysis produced:

* **r = -0.400**
* **p < 0.001**

### 4. Group Comparison & Effect Size

Students were divided into high and low social media use groups based on the mean daily social media usage.

| Group                   | Mean Mental Health Score |    SD |
| ----------------------- | -----------------------: | ----: |
| Lower social media use  |                   75.455 | 7.962 |
| Higher social media use |                   69.503 | 9.496 |

The difference between groups corresponded to a **Cohen's d of approximately -0.68**, indicating a moderate-to-large standardised difference between the two groups.

### 5. Linear Regression

A simple linear regression was used to quantify the relationship between daily social media usage and mental health score.

The fitted model produced:

* **Slope:** -1.541
* **Intercept:** 79.506
* **R²:** approximately 0.160
* **r:** -0.400
* **p < 0.001**

The estimated slope suggests that each additional hour of daily social media use is associated with an estimated **1.54-point** decrease in mental health score.

### 6. Multiple Linear Regression

Subsequently, a multiple linear regression model was developed to investigate whether the relationship remained after accounting for additional behavioural variables. The model explained approximately **23.5%** of the observed variation in mental health scores.

The model included:

* Daily social media hours
* Sleep hours
* Physical activity
* Social isolation

The model produced:

* **R² = 0.235**
* **Adjusted R² = 0.235**
* **n = 15,000**

### 7. Model Diagnostics

Regression assumptions were assessed using residual diagnostics and statistical tests.

The analysis included:

* Residual analysis
* Q-Q plot
* Breusch-Pagan test for heteroscedasticity
* Comparison of conventional OLS standard errors with HC3 robust standard errors

The Breusch-Pagan test indicated evidence of **heteroscedasticity**, meaning that the variance of the residuals was not constant across the range of fitted values.

As a result, **HC3 heteroscedasticity-robust standard errors** were considered when interpreting statistical inference.

The Q-Q plot showed that residuals broadly followed the expected pattern through the centre of the distribution, with greater deviation at the extremes.


## Key Findings

The main findings were:

1. Higher daily social media use was associated with lower mental health scores.
2. The correlation between social media use and mental health was moderate and negative (**r = -0.400**).
3. The relationship was statistically significant (**p < 0.001**).
4. Students in the high social media use group had lower average mental health scores.
5. The group difference produced a moderate-to-large effect size (**Cohen's d ≈ -0.68**).
6. A multiple regression model incorporating additional behavioural variables explained approximately **23.5% of the variance** in mental health scores.
7. Regression diagnostics indicated heteroscedasticity, motivating the use of robust HC3 standard errors for inference.

## Conclusion

Overall, the results support the hypothesis that **daily social media use is negatively associated with mental health score within this dataset**.

The analysis found a **moderate negative linear association** between daily social media usage and mental health score. Students reporting greater daily social media use tended to have lower mental health scores, and this relationship remained relevant when additional behavioural variables were incorporated into a multiple regression model.

While the statistical evidence supports an association within the dataset, the findings should not be interpreted causally. The synthetic nature of the data and the observational design mean that the results are best viewed as an opportunity to demonstrate and practise statistical analysis rather than as evidence about the effects of social media on real-world student mental health.


## Technologies & Libraries

The analysis was conducted in **Python** using:

* **Python**
* **Jupyter Notebook**
* **Pandas** — data manipulation and analysis
* **NumPy** — numerical computation
* **Matplotlib** — data visualisation
* **SciPy** — statistical testing
* **Statsmodels** — regression modelling and statistical inference


## Repository Structure

```text
Social-Media-Mental-Health/
│
├── data/
│   └── student_health_grades.csv
│
├── notebooks/
│   └── social_media_mental_health_analysis.ipynb
│
├── assets/
│   ├── ...
│   └── ...
│
├── report/
│   └── ...
│
├── aisn_ds_pg.py
├── README.md
└── requirements.txt
```

## Reproducing the Analysis

Clone the repository:

```bash
git clone https://github.com/PatrykGulik/social_media_mental_health_analysis.git
cd social_media_mental_health_analysis
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Then open the Jupyter Notebook:

```bash
jupyter lab
```

Run the notebook cells sequentially to reproduce the analysis and visualisations.

## Project Status

**Completed — educational data science project**

The project may be extended in the future with additional modelling, non-linear methods, feature engineering, or alternative statistical approaches.

## Author

**Patryk Gulik**

BSc (Hons) Computer Science | 
University of the Highlands and Islands
