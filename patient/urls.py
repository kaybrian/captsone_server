from django.urls import path
from .views import PatientList, PatientCreate, PatientDetail, HealthVitalCreate, HealthVitalList, HeartRate

urlpatterns = [
    path('patients/', PatientList.as_view(), name='patient-list'),
    path('patients/create/', PatientCreate.as_view(), name='patient-create'),
    path('patients/heart-rate-data/', HeartRate.as_view(), name='heart_rate_data'),
    path('patients/<int:pk>/', PatientDetail.as_view(), name='patient-detail'),
    path('patients/<int:patient_id>/vitals/', HealthVitalList.as_view(), name='health-vital-list'),
    path('patients/<int:patient_id>/vitals/create/', HealthVitalCreate.as_view(), name='health-vital-create'),
]

