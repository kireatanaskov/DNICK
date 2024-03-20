from django.contrib import admin
from .models import *
# Register your models here.


class BusinessHoursInlineAdmin(admin.TabularInline):
    model = BusinessHours
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',) # koi polinja za restoranot da se pokazuvaat na index page vo tabelata
    list_filter = ('capacity', 'name',) # spored so da moze da se filtrira

    inlines = [BusinessHoursInlineAdmin]

    # posebni delovi za da ne bide vo eden del da vnesuvas site informacii tuku da se razdelat vo eden del kontakt
    # vo dr working houts
    fieldsets = [
        (None, {'fields': ['name', 'address', 'capacity']}),
        ('Contact', {'fields': ['email', 'phone',]})
    ]

    # definira koj da ima permisija da go izbrise restorantot
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class EmployeeAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def has_change_permission(self, request, obj=None):
        # proveruva dali postoe object Employee ili se kreira nov i dali user so go kreiral
        # e istiot user so go prave baranjeto
        if obj and obj.user == request.user:
            return True
        return False

    def save_model(self, request, obj, form, change):
        # pri kreiranje na nov Employee, na poleto user od objektot mu go dodeluva userot so go prave baranjeto
        obj.user = request.user
        return super(EmployeeAdmin, self).save_model(request, obj, form, change)


class DishAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(DishRestaurant)
admin.site.register(Employees, EmployeeAdmin)
admin.site.register(BusinessHours)
