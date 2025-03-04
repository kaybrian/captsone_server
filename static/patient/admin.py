from django.contrib import admin
from .models import HealthVital, Patient


class HealthVitalAdmin(admin.ModelAdmin):
    list_display = ('patient', 'timestamp', 'blood_pressure', 'heart_rate', 'rest_ecg', 'exang', 'oldpeak', 'risk_score', 'high_risk_probability', 'low_risk_probability')
    search_fields = ['patient', 'timestamp']
    list_filter = ('timestamp',)
    ordering = ['-timestamp']
    date_hierarchy = 'timestamp'
    


class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'name', 'age','sex', 'timestamp', 'updated')
    search_fields = ['patient_id', 'name', 'age']
    list_filter = ('sex', 'timestamp')
    ordering = ('-timestamp',)
    date_hierarchy = 'timestamp'
    


admin.site.register(Patient, PatientAdmin)
admin.site.register(HealthVital, HealthVitalAdmin)