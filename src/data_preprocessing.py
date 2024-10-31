import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize,StandardScaler

def preprocess_data(df):
    """
    Preprocess the data before inserting it into the database.

    Parameters:
    data (pd.DataFrame): The data to preprocess.

    Returns:
    pd.DataFrame: The preprocessed data.
    """

    #set features 
    X = df.drop(columns=['stroke'])
    X['gender'] = X['gender'].apply(lambda x : 0 if x=='Female' else 1) # encode gender column

    #set target 
    y = df['stroke']
    
    #split the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    return X_train, X_test, y_train, y_test

