from django.conf import settings
from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User as U

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


OFFICE_CHOICES = (
    ('Head Office', 'Head Office'),
    ('Uttara Branch', 'Uttara Branch'),
    ('Mirpur Branch', 'Mirpur Branch'),
)


class User(AbstractUser):
    office = models.CharField(_('Office'), max_length=20, choices=OFFICE_CHOICES)

    def __str__(self):
        return self.username


class Department(models.Model):
    office = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField() 
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse("core:department-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("core:department-delete", kwargs={"pk": self.pk})
    

class Category(models.Model):
    department = models.ForeignKey(Department, models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    
    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse("core:category-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("core:category-delete", kwargs={"pk": self.pk})
    


class Product(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("core:product-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("core:product-delete", kwargs={"pk": self.pk})
    
    
    
    
