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
print()
print(heart.dtypes)
print()
# rename the 'num' column to 'heart_disease'
heart.rename(columns = {'num': 'heart_disease'}, inplace=True)
print(heart['heart_disease'].value_counts())
print(heart.columns)