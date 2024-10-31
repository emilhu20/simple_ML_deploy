
from utils.data_loading import get_csv_data
from config import data_path, CLOUD_CONFIG
from db.queries import delete_query, fetch_query, insert_query, update_query
from db.setup import create_database, create_table
from src.data_preprocessing import preprocess_data
from src.logistic_regression_model import train_logistic_regression
from src.random_forest_model import train_random_forest
from src.evaluate import evaluate_model
import joblib
from utils.data_loading import load_data_from_bigquery



if __name__ == "__main__":
    #STEP 1: create database and tables
    #create_database()
    #create_table("sql/persons_table.sql")

    #STEP 2: load data
    #data = get_csv_data(data_path)

    #STEP 3: insert data into the table
    #read the sql file and insert the data
    #insert_query("sql/insert_csv_file_manual.sql", data)

    #STEP 4: fetch data from the table
    #df = load_data_from_bigquery(CLOUD_CONFIG['project_id'], CLOUD_CONFIG['dataset'], CLOUD_CONFIG['table'])
    df = fetch_query("sql/get_all_data.sql")
    print(df)

    #STEP 5: preprocess data¨
    X_train, X_test, y_train, y_test = preprocess_data(df)

    #STEP 7: train the model
    LogisticRegressionModel = train_logistic_regression(X_train, y_train)
    RandomForestModel = train_random_forest(X_train, y_train)

    #STEP 8: make predictions
    accuracy_log = evaluate_model(LogisticRegressionModel, X_test, y_test)
    accuracy_rf = evaluate_model(RandomForestModel, X_test, y_test)

    #save model in folder models 
    joblib.dump(LogisticRegressionModel, "models/logistic_regression_model.pkl")
    joblib.dump(RandomForestModel, "models/random_forest_model.pkl")














