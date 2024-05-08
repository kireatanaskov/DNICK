from django.http import HttpResponse, Http404
from django.shortcuts import render

from restaurant.models import Restaurant, Dish


# Create your views here.
def index(request):
    return render(request, "index.html")


def restaurants(request):
    restaurants1 = Restaurant.objects.all()

    return render(request, "restaurants.html", {"restaurants": restaurants1, "new_var": 1})


def restaurant_details(request, restaurant_id):
    restaurant  = Restaurant.objects.get(id=restaurant_id)

    return HttpResponse(f"<p>Restaurant details for restaurant with id = {restaurant_id}.</p>"
                        f"<p>Restaurant name: {restaurant.name}, capacity: {restaurant.capacity}</p>")


def dishes(request):
    dishes1 = Dish.objects.all()

    return render(request, "dishes.html", {"dishes": dishes1, "count": len(dishes1)})


def dish_details(request, dish_id):
    try:
        dish = Dish.objects.get(id=dish_id)
    except Dish.DoesNotExist:
        raise Http404("Dish does not exists!")

    return HttpResponse(dish)
