from django.db import models
from django.contrib.auth.models import User

class Office(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    office = models.ForeignKey(Office, models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField() 
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    department = models.ForeignKey(Department, models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    stock = models.PositiveIntegerField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("core:product-list", kwargs={"pk": self.pk})
    
    
    
    
