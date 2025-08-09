from django.shortcuts import render, redirect
from .models import Car

def index(request):
    cars = Car.objects.all()
    return render(request, "Product_App/cars.html", {"cars": cars})

def add_car(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')

        if name and price:
            Car.objects.create(name=name, price=price)
            return redirect('index')  # Redirect to index view after saving

    cars = Car.objects.all()
    return render(request, "Product_App/cars.html", {"cars": cars})
