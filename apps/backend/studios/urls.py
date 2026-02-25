from django.urls import path
from . import views

app_name = "studios"
urlpatterns = [
    path('', views.StudioListCreate.as_view(), name='studio-list-create'),
    path('<int:pk>/', views.StudioDetail.as_view(), name='studio-detail'),
]