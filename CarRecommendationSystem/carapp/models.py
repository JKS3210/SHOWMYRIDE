from django.db import models

# Create your models here.
class CarDetails(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    selling_price=models.IntegerField()
    km_driven=models.IntegerField()
    fuel=models.CharField(max_length=20)
    seller_type=models.CharField(max_length=50)
    transmission=models.CharField(max_length=50)
    owner=models.CharField(max_length=50)
    mileage=models.CharField(max_length=50)
    engine=models.CharField(max_length=50)
    max_power=models.CharField(max_length=50)
    torque=models.CharField(max_length=50)
    seats=models.IntegerField()