from rest_framework import viewsets
from .models import Provider, Appointment
from .serializers import ProviderSerializer, AppointmentSerializer

# Create your views here.
class ProviderViewSet(viewsets.ModelViewSet):
    # queryset = Provider.objects.all() # .order_by('full_name')
    serializer_class = ProviderSerializer

    def get_queryset(self):
        """
        Restricts on name, specialty
        """
        queryset = Provider.objects.all()

        # Get params
        name = self.request.query_params.get('name', None)
        specialty = self.request.query_params.get('specialty', None)

        if name is not None:
            queryset = queryset.filter(full_name__contains=name)

        if specialty is not None:
            queryset = queryset.filter(specialty__contains=specialty)

        return queryset

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
