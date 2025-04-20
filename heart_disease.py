import pandas as pd

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
print(heart.shape)
print(heart.dtypes)