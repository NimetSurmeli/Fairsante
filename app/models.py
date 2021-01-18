from django.db import models

class Product (models.Model):
    brand = models.CharField(max_length=100)
    pname = models.CharField(max_length=200, verbose_name='ProductName')

    def __str__(self):
        return self.pname


# Create your models here.
class Ingredient (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rate = models.IntegerField(max_length=2)

    def __str__(self):
        return self.product.pname + " - " + self.name



