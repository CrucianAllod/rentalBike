from django.db import models
from django.contrib.auth.models import User

class Bike(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    bikes_type = models.CharField(max_length=50)
    max_load = models.IntegerField(blank=True, null=True)
    free_status = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    age_group = models.ForeignKey('AgeGroup', on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.model} | {self.bikes_type}'
    
    class Meta:
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипеды'

class AgeGroup(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Возрастная группа'
        verbose_name_plural = 'Возрастные группы'
    

class Rental(models.Model):
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField(default=None, null=True)
    cost = models.DecimalField(max_digits=9, decimal_places=2, editable=False, null=True, blank=True)
    bike = models.ForeignKey('Bike', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.time_start}-{self.time_end} | {self.cost} | {self.user.last_name} {self.user.first_name}'
    
    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'