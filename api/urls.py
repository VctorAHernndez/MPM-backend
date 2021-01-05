from django.urls import include, path
from rest_framework import routers
from .views import ProviderViewSet, AppointmentViewSet

router = routers.DefaultRouter()
router.register(r'providers', ProviderViewSet, basename='providers')
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
