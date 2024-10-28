
CREATE TABLE IF NOT EXISTS persons (
    id INT PRIMARY KEY,
    gender VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    hypertension INT NOT NULL,
    heart_disease INT NOT NULL,
    ever_married VARCHAR(10) NOT NULL,
    work_type VARCHAR(20) NOT NULL,
    residence_type VARCHAR(10) NOT NULL,
    avg_glucose_level FLOAT NOT NULL,
    bmi FLOAT,
    smoking_status VARCHAR(255) NOT NULL,
    stroke INT NOT NULL
);