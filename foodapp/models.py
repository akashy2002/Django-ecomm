from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(
        max_length=100, default="", null=True, blank=True)
    cat_img = models.ImageField(upload_to="category/")

    def __str__(self):
        return self.cat_name


class Fooditem(models.Model):
    food_name = models.CharField(max_length=100, null=True, blank=True)
    food_img = models.ImageField(upload_to="fooditem")
    food_description = models.TextField(max_length=500, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name


class Order(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.BigIntegerField(default=0, null=True, blank=True)
    price = models.BigIntegerField(default=0, null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(Fooditem, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.Fooditem.food_name
