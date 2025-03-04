from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, HealthVital
from .serializers import PatientSerializer, HealthVitalSerializer
from django.http import JsonResponse
from django.db.models import Avg
from datetime import timedelta, date
from django.utils import timezone

class PatientList(APIView):
    def get(self, request):
        """
        Retrieve a list of all patients.

        This method queries the database for all Patient records, serializes
        them using the PatientSerializer, and returns the serialized data
        in the response.

        Args:
            request (HttpRequest): The request object containing request data.

        Returns:
            Response: A Response object containing serialized patient data.
        """

        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

class PatientCreate(APIView):
    def post(self, request):
        """
        Create a new patient record.

        This method takes in request data, validates it against the PatientSerializer,
        and saves it as a new Patient record if the data is valid. It returns a Response
        object with the serialized patient data and a status code indicating success or
        failure of the creation process.

        Args:
            request (HttpRequest): The request object containing the patient data
                                to be created.

        Returns:
            Response: A Response object containing serialized patient data and a status
                    code of HTTP_201_CREATED if the data is valid and the patient is
                    successfully created, or serialized error data and a status code
                    of HTTP_400_BAD_REQUEST if the data is invalid.
        """

        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetail(APIView):
    def get_object(self, pk):
        """
        Return a Patient object with the given pk, or None if no such patient exists.

        Args:
            pk (int): The primary key of the patient to retrieve.

        Returns:
            Patient: The patient with the given pk, or None if no such patient exists.
        """
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return None

    def get(self, request, pk):
        """
        Retrieve a patient record with the given pk.

        This method takes in a request containing the pk of the patient to
        retrieve, queries the database for the corresponding patient record,
        serializes it using the PatientSerializer, and returns the serialized
        data in the response.

        Args:
            request (HttpRequest): The request object containing the pk of the
                                patient to retrieve.
            pk (int): The primary key of the patient to retrieve.

        Returns:
            Response: A Response object containing serialized patient data and
                    a status code indicating success or failure of the retrieval
                    process.
        """
        patient = self.get_object(pk)
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update an existing patient record with the given pk.

        This method takes in a request containing the pk of the patient to update
        and the data to update the patient record with. It queries the database
        for the corresponding patient, validates the request data against the
        PatientSerializer, and updates the patient record if the data is valid.
        Returns a Response object with the serialized patient data and a status
        code indicating success or failure of the update process.

        Args:
            request (HttpRequest): The request object containing the data to
                                update the patient with.
            pk (int): The primary key of the patient to update.

        Returns:
            Response: A Response object containing serialized patient data and
                    a status code of HTTP_200_OK if the data is valid and the
                    patient is successfully updated, or serialized error data
                    and a status code of HTTP_400_BAD_REQUEST if the data is
                    invalid, or a status code of HTTP_404_NOT_FOUND if no such
                    patient exists.
        """

        patient = self.get_object(pk)
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete an existing patient record with the given pk.

        This method takes in a request containing the pk of the patient to delete,
        queries the database for the corresponding patient, and deletes the record
        if the patient exists. Returns a Response object with a status code
        indicating success or failure of the deletion process.

        Args:
            request (HttpRequest): The request object containing the pk of the
                                patient to delete.
            pk (int): The primary key of the patient to delete.

        Returns:
            Response: A Response object with a status code of HTTP_204_NO_CONTENT
                    if the patient is successfully deleted, or a status code of
                    HTTP_404_NOT_FOUND if no such patient exists.
        """
        patient = self.get_object(pk)
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HealthVitalCreate(APIView):
    def post(self, request, patient_id):
        """
        Create a new health vital record for the patient with the given patient_id.

        This method takes in a request containing the health vital data to be
        created, queries the database for the corresponding patient, and creates
        the health vital record if the patient exists and the data is valid.
        Returns a Response object with the serialized health vital data and a
        status code indicating success or failure of the creation process.

        Args:
            request (HttpRequest): The request object containing the health vital
                                data to be created.
            patient_id (int): The primary key of the patient for which to create
                            the health vital record.

        Returns:
            Response: A Response object with the serialized health vital data and
                    a status code of HTTP_201_CREATED if the data is valid and the
                    health vital record is successfully created, or a status code
                    of HTTP_400_BAD_REQUEST if the data is invalid, or a status
                    code of HTTP_404_NOT_FOUND if no such patient exists.
        """
        try:
            patient = Patient.objects.get(pk=patient_id)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = HealthVitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HealthVitalList(APIView):
    def get(self, request, patient_id):
        """
        Retrieve a list of all health vitals for the patient with the given patient_id.

        This method queries the database for all HealthVital records associated
        with the given patient, serializes them using the HealthVitalSerializer,
        and returns the serialized data in the response.

        Args:
            request (HttpRequest): The request object containing request data.
            patient_id (int): The primary key of the patient for which to retrieve
                            the health vitals.

        Returns:
            Response: A Response object containing serialized health vital data and
                    a status code of HTTP_200_OK if the patient exists and the
                    health vitals are successfully retrieved, or a status code
                    of HTTP_404_NOT_FOUND if no such patient exists.
        """
        
        try:
            patient = Patient.objects.get(pk=patient_id)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        vitals = patient.vitals.all()
        serializer = HealthVitalSerializer(vitals, many=True)
        return Response(serializer.data)


class HeartRate(APIView):
    def get(self, request):
        today = timezone.now().date() 
        last_7_days = today - timedelta(days=6)  

        heart_rates = (
            HealthVital.objects
            .filter(timestamp__date__range=[last_7_days, today])
            .values("timestamp__date")  
            .annotate(avg_heart_rate=Avg("heart_rate"))  
            .order_by("timestamp__date")
        )

        # Convert data for JavaScript
        data = {
            "dates": [entry["timestamp__date"].strftime("%Y-%m-%d") for entry in heart_rates],
            "avgHeartRates": [entry["avg_heart_rate"] for entry in heart_rates],
        }

        return Response(data, status=status.HTTP_200_OK)