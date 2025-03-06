from patient.models import Patient, HealthVital
from django.db.models import Avg


# define a function to get patient number of female and male
def getPatientGender():
    male = Patient.objects.filter(sex=1).count()
    female = Patient.objects.filter(sex=0).count()
    return male, female


# create a function that gets the total
def getAveragePatientVitals():
    # Aggregate all vitals directly from the database
    avg_vitals = HealthVital.objects.aggregate(
        avg_blood_pressure=Avg("blood_pressure"),
        avg_heart_rate=Avg("heart_rate"),
        avg_rest_ecg=Avg("risk_score"),
    )

    # Handle cases where no records exist
    average_blood_pressure = avg_vitals["avg_blood_pressure"] or 0
    average_heart_rate = avg_vitals["avg_heart_rate"] or 0
    average_rest_ecg = avg_vitals["avg_rest_ecg"] or 0

    return (
        round(average_blood_pressure, 2),
        round(average_heart_rate, 2),
        round(average_rest_ecg, 2),
    )

