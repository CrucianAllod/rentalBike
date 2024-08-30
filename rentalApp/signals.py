from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Rental, Bike



@receiver(post_save, sender=Rental)
def stop_free_status(instance, created, **kwargs):
    if created:
        instance.bike.free_status = False
        instance.bike.save(update_fields=['free_status'])

@receiver(post_save, sender=Rental)
def stop_free_status(instance, created, **kwargs):
    if instance.time_end != None:
        instance.bike.free_status = True
        instance.bike.save(update_fields=['free_status'])