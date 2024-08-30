from rest_framework import generics, serializers
from rest_framework import status
from rest_framework.response import Response


from .serializers import BikeSerializer, RefundBikeSerializer, RentalSerializer

from .models import Bike, Rental

from .async_task import calculate_cost, my_task, send_cost_to_user


class BikeAPIList(generics.ListAPIView):
    queryset = Bike.objects.filter(free_status=True)
    serializer_class = BikeSerializer

class RentalAPICreate(generics.CreateAPIView):
    serializer_class = RentalSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        rentals = Rental.objects.filter(user=user_id)
        for open_rental in rentals:
            if open_rental.time_end == None:
                return Response({'error': 'У вас есть незакрытая аренда'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class RentalAPIList(generics.ListAPIView):
    serializer_class = RentalSerializer

    def get_queryset(self):
        return Rental.objects.filter(user=self.request.user)
    

class RefundBikeAPI(generics.UpdateAPIView):
    serializer_class = RefundBikeSerializer

    def get_object(self):
        user = self.request.user
        try:
            return Rental.objects.filter(user=user).latest('time_start')
        except Rental.DoesNotExist:
            raise serializers.ValidationError('У вас нет активных аренд')

    def update(self, request, *args, **kwargs):
        instance = self.get_object()    
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # task = calculate_cost.apply_async(args=[instance.id])
        task = my_task.apply_async(args=[3,4])
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)