import pandas as pd
import numpy as np

# column names for the dataset
# The dataset is from the UCI Machine Learning Repository
# https://archive.ics.uci.edu/ml/datasets/heart+Disease
column_names = ['age', 
                'sex', 
                'cp', 
                'trestbps', 
                'chol', 
                'fbs', 
                'restecg', 
                'thalach', 
                'exang', 
                'oldpeak', 
                'slope', 
                'ca', 
                'thal', 
                'num']

heart = pd.read_csv('./heart+disease/processed.cleveland.data', names=column_names)
print(heart.head())
print()
print(heart.dtypes)
print()
# rename the 'num' column to 'heart_disease'
heart.rename(columns = {'num': 'heart_disease'}, inplace=True)
print(heart['heart_disease'].value_counts())
print(heart.columns)

print()
print(heart.info())
print()

print(heart[(heart['ca']=='?')])
# replace '?' with np.nan
heart = heart.replace('?', np.nan)
print(heart['ca'].unique())
print()
print(heart['thal'].unique())