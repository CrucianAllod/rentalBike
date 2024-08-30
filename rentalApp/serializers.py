from rest_framework import serializers
from .models import Bike, Rental


class BikeSerializer(serializers.ModelSerializer):
    age_group = serializers.SerializerMethodField()

    def get_age_group(self, obj):
        return obj.age_group.title if obj.age_group else None
    
    class Meta:
        model = Bike
        fields = "__all__"
        
    def get_queryset(self):
        return Bike.objects.filter(free_status=True)    

class RentalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    time_end = serializers.HiddenField(default=None)
    bike = serializers.PrimaryKeyRelatedField(queryset=Bike.objects.filter(free_status=True))
    
    class Meta:
        model = Rental
        exclude  = ['cost']

class RefundBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['time_end']
