from django.urls import path
from . import views

app_name = "studios"

urlpatterns = [
    path('studios/', views.StudioListCreate.as_view(), name='studio-list-create'),
    path('studios/<int:pk>/', views.StudioDetail.as_view(), name='studio-detail'),
    path('owners/<int:pk>/', views.OwnerDetail.as_view(), name='owner-detail'),
]