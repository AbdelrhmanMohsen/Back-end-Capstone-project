from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=1)
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    

class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.SmallIntegerField(default=6)
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.name} for {self.number_of_guests} guests on {self.booking_date}'

