from django.urls import path, include
from .views import SearchLocationAPIView

urlpatterns = [
    path('search/', SearchLocationAPIView.as_view(), name="search_weather"),
]
