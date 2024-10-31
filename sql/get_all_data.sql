

SELECT id, gender, hypertension, heart_disease, avg_glucose_level, bmi, stroke
from persons
where bmi is not null
