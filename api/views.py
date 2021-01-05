from rest_framework import viewsets, status
from django.http import JsonResponse
from django.db.models import Q
from .models import Provider, Appointment
from .serializers import ProviderSerializer, AppointmentSerializer

# Create your views here.
class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer

    def get_queryset(self):
        queryset = Provider.objects.all()

        query = self.request.query_params.get('q', None)
        name = self.request.query_params.get('name', None)
        specialty = self.request.query_params.get('specialty', None)

        if query is not None:
            combined_filter = Q(full_name__icontains=query) | Q(specialty__icontains=query)
            queryset = queryset.filter(combined_filter)

        if name is not None:
            queryset = queryset.filter(full_name__icontains=name)

        if specialty is not None:
            queryset = queryset.filter(specialty__icontains=specialty)

        return queryset

# TODO: Prevent appointments from clashing by responding with 400
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        phone = data.get('patient_phone_number', None)
        serializer = AppointmentSerializer(data=data)

        # TODO: Improve with refactoring hard-coded values
        # App-level validation doesn't occur at Model, so we validate min_length here
        if serializer.is_valid() and phone is not None and len(phone) >= 9:
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({
            'patient_phone_number': ['Phone number must have a minimum of 9 digits.']
            },
            status=status.HTTP_400_BAD_REQUEST
        )
