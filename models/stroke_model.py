#write hello world

import numpy as np
import pandas as pd



def initialize_model():
    # Load the dataset
    data = pd.read_csv('data/stroke_data.csv')

    # Drop the id column
    data = data.drop('id', axis=1)

    # Fill missing values
    data['bmi'] = data['bmi'].fillna(data['bmi'].mean())

    # Encode categorical columns
    data = pd.get_dummies(data, columns)



def train_model(data):
    # Split the data into features and target
    X = data.drop('stroke', axis=1)
    y = data['stroke']

    # Split the data into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a logistic regression model
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    return model

