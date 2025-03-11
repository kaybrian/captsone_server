from django.shortcuts import render
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from patient.models import Patient, HealthVital
from .utils import getPatientVitals


@login_required()
def addUser(request):
    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        name = request.POST['name']
        age = request.POST['age']
        sex = request.POST['sex']
        
        if Patient.objects.filter(patient_id=patient_id).exists():
            return HttpResponseRedirect('/users/addUser')
        
        # change the sx to 1 if male and 0 if female
        if sex.lower() == 'male':
            sex = 1
        else:
            sex = 0
        
        patient = Patient(patient_id=patient_id, name=name, age=age, sex=sex)
        patient.save()
        return HttpResponseRedirect('/users/users-list')
      
    
    context={
        "title": "Add User",
        "subTitle": "Add User",
    }
    return render(request, "users/addUser.html", context)


@login_required()
def usersGrid(request):
    context={
        "title": "Users Grid",
        "subTitle": "Users Grid",
    }
    return render(request, "users/usersGrid.html", context)

@login_required()
def usersList(request):
    patients = Patient.objects.all()
    
    # add the patient to the context 
    context={
        "title": "Users List",
        "subTitle": "Users List",
        "patients": patients,
    }
    return render(request, "users/usersList.html", context)


@login_required()
def viewProfile(request):        
    context={
        "title": "View Profile",
        "subTitle": "View Profile",
    }
    return render(request, "users/viewProfile.html", context)



@login_required()
def viewPatientProfile(request, patient_id):
    if request.method == "POST":
        # update the patient's details
        patient = get_object_or_404(Patient, patient_id=patient_id)
        patient.name = request.POST['name']
        patient.age = request.POST['age']
        
        # change the sx to 1 if male and 0 if female
        if request.POST['gender'].lower() =='male':
            patient.sex = 1
        else:
            patient.sex = 0
        
        patient.save()
        
        return HttpResponseRedirect('/users/view-patient-profile/' + patient_id)
        
    else:
    
        patient = get_object_or_404(Patient, patient_id=patient_id)
        
        # get the health vital of the patient
        health_vitals = HealthVital.objects.filter(patient=patient)
        
        # get the average health of the patient blood_pressure, high_risk_probability
        blood_pressure = 0
        high_risk_probability = 0
        
        for vital in health_vitals:
            blood_pressure += vital.blood_pressure
            high_risk_probability += vital.high_risk_probability
        
        # prevent the divide by zero error 
        if len(health_vitals) > 0:
            blood_pressure = blood_pressure / len(health_vitals)
            high_risk_probability = high_risk_probability / len(health_vitals)
        else:
            blood_pressure = 0
            high_risk_probability = 0
        
        
        
        context={
            "title": "View Profile",
            "subTitle": "View Profile",
            "patient": patient,
            "health_vitals": health_vitals,
            "blood_pressure": blood_pressure,
            "high_risk_probability": high_risk_probability
            
        }
        return render(request, "users/viewProfile.html", context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/users/login')
    context={
        "title": "Login",
        "subTitle": "Login",
    }

    return render(request, "authentication/signin.html", context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/users/login')



def userVitals(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)

    # get the health vital of the patient
    health_vitals = getPatientVitals(patient)

    context={
        "title": "User Vitals",
        "subTitle": "View User Vitals",
        "patient": patient,
        "health_vitals": health_vitals,
    }

    return render(request, "users/userVitals.html", context)
    