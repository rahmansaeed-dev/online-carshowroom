from django.contrib import admin
from .models import Car, Company

# Register your models here.

admin.site.register(Car)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['company','name','model','year','price','color_options','engine_type','transmission_type','image','img1','img2','img3']

admin.site.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ['name','description','office_image',]




