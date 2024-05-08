from django.contrib import admin
from django.urls import path

from restaurant.views import index, restaurants, restaurant_details, dishes, dish_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('restaurants/', restaurants, name="restaurants"),
    path('restaurant_details/<int:restaurant_id>/', restaurant_details, name="restaurant Details"),
    path('dishes/', dishes, name="dishes"),
    path('dish_details/<int:dish_id>', dish_details, name="dish details")
]
