from django.shortcuts import render
from .models import Car, Driver

# Create your views here.

def car_detail(request, pk):
    owner_obj = Driver.objects.get(pk=pk)
    car_objects = Car.objects.filter(owner_id=owner_obj.id)

    context = {
        'vehicles': car_objects,
        'drivers' : owner_obj,
    }

    return render(request, 'car_detail.html', context)
