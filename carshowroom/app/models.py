from django.db import models

# Company model
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    office_image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.name


# Car model 
class Car(models.Model):
    company = models.ForeignKey(Company, related_name='cars', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color_options = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)
    transmission_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='car_images/')
    img1 = models.ImageField(upload_to='car_images/', blank=True, null=True)
    img2 = models.ImageField(upload_to='car_images/', blank=True, null=True)
    img3 = models.ImageField(upload_to='car_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.model}"
