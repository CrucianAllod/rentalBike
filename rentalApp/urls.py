from django.contrib import admin
from django.urls import path
from .views import BikeAPIList, RentalAPICreate, RentalAPIList, RefundBikeAPI

app_name = 'rentalApp'


urlpatterns = [
    path('bikelist/', BikeAPIList.as_view()),
    path('rental/', RentalAPICreate.as_view()),
    path('rentaList/', RentalAPIList.as_view()),
    path('refund/', RefundBikeAPI.as_view()),
]
