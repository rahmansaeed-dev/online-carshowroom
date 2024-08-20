from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('base/', views.base, name='base'),
    path('category/', views.car_category, name= 'category'),
    path('detail/<int:id>/', views.car_detail, name='detail'),
    path('company/<int:company_id>/', views.company_cars_view, name='company_cars'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)