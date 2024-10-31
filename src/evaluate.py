from sklearn.metrics import accuracy_score, roc_auc_score


def evaluate_model(model, X_test, y_test):
    # Predict labels
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]  # Probability estimates for AUC

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred_proba)
    
    print(f"Accuracy: {accuracy}")
    print(f"AUC: {auc}")
    
    return {"accuracy": accuracy, "auc": auc}


