import os
import django

# Setup Django settings FIRST, before any other imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HealthData.settings')
django.setup()

# Now import everything else after Django is configured
import random
from faker import Faker
from datetime import datetime, timedelta
from django.db.utils import IntegrityError
from patient.models import Patient, HealthVital

fake = Faker()


def generate_patient_id():
    """Generate a unique patient ID"""
    return f'P00{random.randint(1, 20)}'

def create_patients(n=10):
    """Create only 10 patients"""
    patients = []
    for _ in range(n):
        try:
            patient = Patient.objects.create(
                patient_id=generate_patient_id(),
                name=fake.name(),
                age=random.randint(18, 90),
                sex=random.choice([0, 1]),
                is_active=random.choices([True, False], weights=[0.9, 0.1])[0] 
            )
            patients.append(patient)
        except IntegrityError:
            print("Duplicate patient ID encountered, retrying...")
            continue
    
    print(f"Successfully created {len(patients)} patients")
    return patients

def generate_random_timestamp():
    """Generate a random timestamp within the last 6 months"""
    today = datetime.now()
    start_date = today - timedelta(days=180)  # 6 months ago
    random_days = random.randint(0, 180)
    random_time = timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
    return start_date + timedelta(days=random_days) + random_time

def generate_realistic_vitals():
    """Generate realistic vital signs"""
    blood_pressure = random.randint(90, 180)
    heart_rate = random.gauss(80, 10)  # mean of 80, std dev of 10
    heart_rate = max(min(heart_rate, 120), 60)  # Clamp between 60 and 120
    rest_ecg = random.choices([0, 1, 2], weights=[0.7, 0.2, 0.1])[0]
    exang = random.choices([0, 1], weights=[0.8, 0.2])[0]
    oldpeak = round(random.uniform(0, 4), 1)

    base_risk = (blood_pressure - 90)/90 * 30 + \
                (abs(heart_rate - 80)/20 * 20) + \
                (rest_ecg * 15) + \
                (exang * 20) + \
                (oldpeak * 5)
    
    risk_score = min(100, max(0, base_risk))
    high_risk_prob = risk_score if risk_score > 50 else 100 - risk_score
    low_risk_prob = 100 - high_risk_prob

    return {
        'blood_pressure': blood_pressure,
        'heart_rate': heart_rate,
        'rest_ecg': rest_ecg,
        'exang': exang,
        'oldpeak': oldpeak,
        'risk_score': risk_score,
        'high_risk_probability': high_risk_prob,
        'low_risk_probability': low_risk_prob,
        'timestamp': generate_random_timestamp()
    }

def create_health_vitals(patients, n=1000):
    """Create vitals over time for 10 patients"""
    vitals_created = 0
    batch_size = 500  # Create records in batches
    
    while vitals_created < n:
        vitals_to_create = min(batch_size, n - vitals_created)
        vitals_list = []
        
        for _ in range(vitals_to_create):
            patient = random.choice(patients)
            vitals_data = generate_realistic_vitals()
            
            vital = HealthVital(
                patient=patient,
                **vitals_data
            )
            vitals_list.append(vital)
        
        # Bulk create the batch
        HealthVital.objects.bulk_create(vitals_list)
        vitals_created += vitals_to_create
        print(f"Created {vitals_created} of {n} health vitals...")

if __name__ == "__main__":
    print("Starting data generation...")
    patients = create_patients(10)
    create_health_vitals(patients, 10000) 
    print("Data generation completed!")
