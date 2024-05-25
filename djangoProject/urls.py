from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from restaurant.views import add_employee, add_restaurant, index, restaurants, restaurant_details, dishes, dish_details, \
    edit_restaurant, delete_restaurant

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('index/', index, name="index"),
    path('restaurants/', restaurants, name="restaurants"),
    path('restaurant_details/<restaurant_id>/', restaurant_details, name="restaurant details"),
    path('restaurant/edit/<id>/', edit_restaurant, name="edit restaurant"),
    path('dishes/', dishes, name="dishes"),
    path('dish_details/<int:dish_id>', dish_details, name="dish details"),
    path('add_restaurant/', add_restaurant, name="Add restaurant"),
    path('delete_restaurant/<id>', delete_restaurant, name="delete restaurant"),
    path('add_employee/', add_employee, name="add employee"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
