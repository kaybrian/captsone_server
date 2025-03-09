from patient.models import Patient, HealthVital
from django.db.models import Avg, Count, Q, F, Max
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Case, When, IntegerField

# define a function to get patient number of female and male
def getPatientGender():
    """
    Return a tuple containing the count of male and female patients.

    Returns:
        tuple: A tuple of two integers, the first is the count of male patients
            and the second is the count of female patients.
    """
    male = Patient.objects.filter(sex=1).count()
    female = Patient.objects.filter(sex=0).count()
    return male, female


# create a function that gets the total
def getAveragePatientVitals():
    # Aggregate all vitals directly from the database
    """
    Return the average of blood pressure, heart rate, and resting ECG risk score for all patients.

    Returns:
        tuple: A tuple of three floats, representing the average blood pressure, heart rate, and resting ECG risk score, respectively.
    """
    
    avg_vitals = HealthVital.objects.aggregate(
        avg_blood_pressure=Avg("blood_pressure"),
        avg_heart_rate=Avg("heart_rate"),
        avg_rest_ecg=Avg("rest_ecg"),  
        avg_risk_score=Avg("risk_score")
    )

    # Handle cases where no records exist
    average_blood_pressure = avg_vitals["avg_blood_pressure"] or 0
    average_heart_rate = avg_vitals["avg_heart_rate"] or 0
    average_rest_ecg = avg_vitals["avg_rest_ecg"] or 0
    average_risk_score = avg_vitals["avg_risk_score"] or 0
    
    return (
        round(average_blood_pressure, 2),
        round(average_heart_rate, 2),
        round(average_rest_ecg, 2),
        round(average_risk_score, 2),
    )


def get_age_distribution():
    """
    Categorize patients into age groups.

    This function calculates the number of patients in each age group: pediatric (age <= 18),
    adult (age > 18 and age <= 65), and senior (age > 65).

    Parameters:
    None

    Returns:
    dict: A dictionary containing the count of patients in each age group. The keys are 'pediatric', 'adult', and 'senior'.
    """
    return Patient.objects.aggregate(
        pediatric=Count("id", filter=Q(age__lte=18)),
        adult=Count("id", filter=Q(age__gt=18, age__lte=65)),
        senior=Count("id", filter=Q(age__gt=65)),
    )


def get_risk_distribution():
    """
    Categorize health vitals into risk groups.

    This function calculates the number of health vitals in each risk group: low risk (risk score < 30),
    medium risk (risk score >= 30 and risk score < 70), and high risk (risk score >= 70).

    Parameters:
    None

    Returns:
    dict: A dictionary containing the count of health vitals in each risk group. The keys are 'low_risk', 'medium_risk', and 'high_risk'.
    """
    return HealthVital.objects.aggregate(
        low_risk=Count("id", filter=Q(risk_score__lt=30)),
        medium_risk=Count("id", filter=Q(risk_score__gte=30, risk_score__lt=70)),
        high_risk=Count("id", filter=Q(risk_score__gte=70)),
    )


def get_active_patients():
    """
    Count the number of active and inactive patients.

    This function returns a tuple containing two values, the first is the count of active patients
    and the second is the count of inactive patients.

    Parameters:
    None

    Returns:
    tuple: a tuple containing the count of active patients and the count of inactive patients.
    """
    active = Patient.objects.filter(is_active=True).count()
    inactive = Patient.objects.filter(is_active=False).count()
    return active, inactive

def get_critical_alerts():
    """
    Retrieve the most recent critical health alerts for up to 5 unique patients.

    Conditions for critical health alerts:
    - Blood pressure (BP) >= 140
    - Heart rate (HR) < 50 or HR > 120

    Ensures that each patient appears only once (most recent record).
    Returns:
        QuerySet: A list containing up to 5 unique patients with critical alerts.
    """

    # Get the latest vital record timestamp per patient where conditions are met
    latest_critical_vitals = HealthVital.objects.filter(
        Q(blood_pressure__gte=140) | Q(heart_rate__lt=50) | Q(heart_rate__gt=120)
    ).values("patient").annotate(latest_timestamp=Max("timestamp"))

    # Use the latest timestamp to fetch actual records
    alerts = HealthVital.objects.filter(
        Q(blood_pressure__gte=10) | Q(heart_rate__lt=10) | Q(heart_rate__gt=10),
        timestamp__in=[entry["latest_timestamp"] for entry in latest_critical_vitals]
    ).order_by("-timestamp").values(
        "patient__name", 
        "patient_id",
        "blood_pressure", 
        "heart_rate",
        "high_risk_probability", 
        "low_risk_probability",
    )[:5]

    return alerts


def get_iot_device_status():
    """
    Check if there has been any health vital data received in the last 2 hours.

    This function is used to determine if the IoT device is currently active or not.
    It queries the HealthVital database for any records with a timestamp from the last 2 hours.
    If there are any records, it returns True, otherwise it returns False.

    Parameters:
    None

    Returns:
    bool: True if there has been any health vital data received in the last 2 hours, otherwise False
    """
    threshold = timezone.now() - timedelta(hours=2)
    return HealthVital.objects.filter(timestamp__gte=threshold).exists()

