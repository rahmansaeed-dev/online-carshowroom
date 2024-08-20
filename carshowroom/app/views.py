from django.shortcuts import render, get_object_or_404
from .models import Car, Company
# Create your views here.

# base page view 
def base(request):
    return render(request, 'base.html')

# home page view
def Home(request):
    company = Company.objects.all()
    print(company)
    contaxt = {'company':company}
    print(contaxt)
    return render(request, 'index.html', contaxt)

# car category view 
def car_category(request):
    cars = Car.objects.all()
    contaxt = {'cars':cars}
    return render(request, 'category.html', contaxt)

# car detail view 
def car_detail(request, id):
    cars = Car.objects.get(id=id)
    print(cars)
    # print(company_id)
    return render(request, 'detail.html', context={'cars':cars})

# Hyundai view
# def hyundai(request):
#     hundai = Car.objects.filter()
#     return render(request, 'hyndai.html')

# # Audi view
# def Audi(request):
#     return render(request, 'hyndai.html')

# # Suzuki view
# def Suzuki(request):
#     return render(request, 'hyndai.html')


def company_cars_view(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    cars = Car.objects.filter(company=company)
    return render(request, 'hyndai.html', {'company': company, 'cars': cars})
