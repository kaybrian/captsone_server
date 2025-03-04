from rest_framework import serializers
from .models import Patient, HealthVital

class HealthVitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthVital
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    vitals = HealthVitalSerializer(many=True, required=False)

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        vitals_data = validated_data.pop('vitals', [])
        patient = Patient.objects.create(**validated_data)
        for vital_data in vitals_data:
            HealthVital.objects.create(patient=patient, **vital_data)
        return patient

    def update(self, instance, validated_data):
        vitals_data = validated_data.pop('vitals', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Optionally delete existing vitals
        if vitals_data:
            instance.vitals.all().delete()
            for vital_data in vitals_data:
                HealthVital.objects.create(patient=instance, **vital_data)

        return instance