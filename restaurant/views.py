from django.http import HttpResponse, Http404
from django.shortcuts import render

from restaurant.forms import NameForm, RestaurantForm, EmployeeForm
from restaurant.models import Restaurant, Dish


# Create your views here.
# def index(request):
#     return render(request, "index.html")


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


def index(request):
    # If this is a POST request we need to process the form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = NameForm(request.POST)
        # Check whether it's valid
        if form.is_valid():
            request.session['your_name'] = form.cleaned_data['your_name']

    # If a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    if 'your_name' not in request.session:
        your_name = "Anonymous"
    else:
        your_name = request.session['your_name']  # add variable to session

    return render(request, "index.html", {"form": form, "your_name": your_name})


def add_restaurant(request):
    if request.method == "POST":
        restaurant = RestaurantForm(request.POST)
        if restaurant.is_valid():
            restaurant.save()
    else:
        restaurant = RestaurantForm()

    return render(request, "add_restaurant.html", {"form": restaurant})


def add_employee(request):
    if request.method == "POST":
        employee = EmployeeForm(request.POST)
        if employee.is_valid():
            if not request.user.is_anonymous:
                employee.instance.user = request.user
                employee.save()
                employee = EmployeeForm()
            else:
                employee.add_error(None, "You must log in.")
        else:
            print(employee.errors)
    else:
        employee = EmployeeForm()

    return render(request, "add_employee.html", {"form": employee})
