from django.db import models

class Patient(models.Model):
    patient_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.IntegerField(choices=[(1, 'Male'), (0, 'Female')])
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        """
        Return a string representation of the Patient.

        Returns the name of the Patient.
        """
        return self.name
    
    class Meta:
        ordering = ['-timestamp']

class HealthVital(models.Model):
    patient = models.ForeignKey(Patient, related_name='vitals', on_delete=models.CASCADE)
    blood_pressure = models.FloatField()
    heart_rate = models.FloatField()
    rest_ecg = models.FloatField()
    exang = models.FloatField()
    oldpeak = models.FloatField()
    risk_score = models.FloatField()
    high_risk_probability = models.FloatField()
    low_risk_probability = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """s
        Return a string representation of the HealthVital instance, including the name of the related patient and the timestamp of the vital signs data.
        """
        return f"Vitals for {self.patient.name} at {self.timestamp}"
    
    class Meta:
        ordering = ['-timestamp']
        
