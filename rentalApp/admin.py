from django.contrib import admin
from .models import AgeGroup, Bike, Rental

admin.site.register(Bike)
admin.site.register(AgeGroup)
admin.site.register(Rental)
