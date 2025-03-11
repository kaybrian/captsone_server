from patient.models import Patient, HealthVital
from datetime import datetime


def getPatientVitals(patient):
    vitals = HealthVital.objects.filter(patient=patient)

    # we need to get each part of the vitals as a single separate one with the dates
    blood_pressure = []
    heart_rate = []
    rest_ecg = []
    oldpeak = []
    exang = []
    risk_score = []
    high_risk_probability = []
    low_risk_probability = []
    timestamp = []

    # go through the vitals and get the values of the variables
    for vital in vitals:
        blood_pressure.append(vital.blood_pressure)
        heart_rate.append(vital.heart_rate)
        rest_ecg.append(vital.rest_ecg)
        oldpeak.append(vital.oldpeak)
        exang.append(vital.exang)
        risk_score.append(vital.risk_score)
        high_risk_probability.append(vital.high_risk_probability)
        low_risk_probability.append(vital.low_risk_probability)
        # convert the timestamp to a string for easier sorting and easier display
        timestamp.append(vital.timestamp.strftime("%Y-%m-%d"))
        
        
    # return it as a list
    return [blood_pressure, heart_rate, rest_ecg, oldpeak, exang, risk_score, high_risk_probability, low_risk_probability, timestamp]