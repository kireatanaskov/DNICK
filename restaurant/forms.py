from django import forms

from restaurant.models import Restaurant, Employees


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name is ", max_length=20)


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"
        exclude = ["user"]
