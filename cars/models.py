from django.db import models

# Create your models here.


class Driver(models.Model):
    name = models.TextField()
    license = models.TextField()

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    vin = models.TextField()
    owner = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
