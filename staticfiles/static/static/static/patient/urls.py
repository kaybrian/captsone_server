from django.urls import path
from .views import PatientList, PatientCreate, PatientDetail, HealthVitalCreate, HealthVitalList

urlpatterns = [
    path('patients/', PatientList.as_view(), name='patient-list'),
    path('patients/create/', PatientCreate.as_view(), name='patient-create'),
    path('patients/<int:pk>/', PatientDetail.as_view(), name='patient-detail'),
    path('patients/<int:patient_id>/vitals/', HealthVitalList.as_view(), name='health-vital-list'),
    path('patients/<int:patient_id>/vitals/create/', HealthVitalCreate.as_view(), name='health-vital-create'),
]

