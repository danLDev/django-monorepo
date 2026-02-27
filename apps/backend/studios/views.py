from django.http import HttpResponse, Http404
from .models import Studio, Booking
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .serializers import StudioSerializer    
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .serializers import OwnerSerializer
from .serializers import BookingSerializer

class StudioFilter(filters.FilterSet):
    max_capacity = filters.NumberFilter()
    max_capacity__gte = filters.NumberFilter(field_name='max_capacity', lookup_expr='gte')
    max_capacity__lte = filters.NumberFilter(field_name='max_capacity', lookup_expr='lte')
    max_capacity__gt = filters.NumberFilter(field_name='max_capacity', lookup_expr='gt')
    max_capacity__lt = filters.NumberFilter(field_name='max_capacity', lookup_expr='lt')
    
    class Meta:
        model = Studio
        fields = ['max_capacity']


class StudioListCreate(ListCreateAPIView):
    """
    List all studios with optional filtering by max_capacity, or create a new studio.
    GET /studios/ - List all studios (use ?max_capacity=50 to filter)
    POST /studios/ - Create a new studio
    """
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudioFilter


class StudioDetail(RetrieveAPIView):
    """
    Retrieve a single studio by ID.
    """
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    
    

class OwnerDetail(RetrieveAPIView):
    """
    Retrieve a single owner by ID.
    """
    queryset = User.objects.all()
    serializer_class = OwnerSerializer


class BookingListCreate(ListCreateAPIView):
    """
    List all studios with optional filtering by max_capacity, or create a new studio.
    GET /studios/ - List all studios (use ?max_capacity=50 to filter)
    POST /studios/ - Create a new studio
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)

class BookingDetail(RetrieveAPIView):
    """
    Retrieve a single studio by ID.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer