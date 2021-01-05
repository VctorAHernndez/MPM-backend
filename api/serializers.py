from rest_framework import serializers
from .models import Provider, Appointment

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'id',
            'full_name',
            'specialty',
            )

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'id',
            'start_time',
            'end_time',
            'appointment_reason',
            'patient_full_name',
            'patient_gender',
            'patient_date_of_birth',
            'patient_phone_number',
            'provider',
            )
