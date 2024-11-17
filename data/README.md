# Customer Churn Prediction

This repository contains a project aimed at predicting customer churn using machine learning. Customer churn refers to the loss of customers, and understanding the factors contributing to it can help businesses improve retention strategies.

## Repository Structure
```
Customer_Churn_Prediction/
│
│
├── data/
│   ├── raw/                      # Raw datasets
│   ├── processed/                # Preprocessed data
│   └── README.md                 # Information about data sources
│
├── notebooks/
│   └── Customer_Churn_Prediction_.ipynb  # Original notebook
│
├── src/
│   ├── data_preprocessing.py     # Scripts for data cleaning and preprocessing
│   ├── feature_engineering.py    # Scripts for feature engineering
│   ├── model_training.py         # Scripts for training models
│   ├── evaluation.py             # Scripts for evaluating models
│   └── __init__.py               # Initialize package
│
├── reports/
│   └── README.md                 # Insights and findings
│
├── tests/
│   ├── test_preprocessing.py     # Unit tests for preprocessing functions
│   ├── test_model_training.py    # Unit tests for model training
│   └── __init__.py               # Initialize test package
│
├── requirements.txt              # Dependencies and libraries
├── README.md                     # Project overview and setup instructions
├── LICENSE                       # Licensing information
└── .gitignore                    # Files to ignore in version control
```


## Features
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Training and evaluating multiple machine learning models
- Model evaluation using key performance metrics

## Steps Taken

### Data Preprocessing:
- Cleaning the dataset by removing duplicates, handling missing values, and standardizing data formats.
- Encoding categorical variables to ensure compatibility with machine learning models.

### Exploratory Data Analysis (EDA):
- Visualizing data distributions, correlations, and feature importance.
- Identifying key factors influencing customer churn, such as contract type, tenure, and monthly charges.

### Feature Engineering:
- Transforming raw features into formats suitable for model training.
- Creating additional derived features to enhance model performance.

### Model Development:
- Training multiple machine learning models, such as logistic regression, decision trees, and random forests.
- Using a train-test split to evaluate model performance and prevent overfitting.

### Evaluation Metrics:
- Accuracy, precision, recall, F1-score, and ROC-AUC were used to evaluate the models.
- Emphasis on recall to minimize the risk of failing to identify potential churners.

### Insights and Recommendations:
- Customers with shorter tenure and higher monthly charges are more likely to churn.
- Flexible contract options and loyalty rewards could improve retention rates.

## Technologies Used
- **Languages:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Tools:** Jupyter Notebook for experimentation and visualization

## Key Features
- Modular scripts for each stage of the project (preprocessing, feature engineering, model training, and evaluation).
- Reproducible results with clear documentation and explanations.
- Insights derived from EDA to guide business strategies.

## Potential Use Cases
- Subscription services (e.g., streaming platforms, SaaS companies).
- Telecom industries aiming to retain customers.
- Any business looking to improve customer retention strategies using data.
