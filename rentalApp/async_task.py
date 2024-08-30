from celery import shared_task
from django.http import JsonResponse
from django.urls import reverse
from.models import Rental


def send_cost_to_user(rental_id):
    url = reverse('get_cost', kwargs={'pk': rental_id})
    data = {'cost': Rental.objects.get(id=rental_id).cost}
    return JsonResponse(data)

@shared_task
def calculate_cost(rental_id):
    rental = Rental.objects.get(id=rental_id)
    bike = rental.bike
    time_start = rental.time_start
    time_end = rental.time_end
    price = bike.price 
    cost = ((time_end-time_start).total_seconds() / 3600) * float(price)
    rental.cost = cost
    rental.save()
    send_cost_to_user(cost)
    return {'cost': cost}  

@shared_task
def my_task(x, y):
    print(f"Мы получили аргументы x={x} и y={y}")
    result = x + y
    print(f"Результат: {result}")
    return result