
# Importing required libraries
from sklearn.linear_model import LogisticRegression

# Model training functions
def train_logistic_regression(X_train, y_train):
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    return model