from django.db import models

# Data Model to pull from database

class Product(models.Model):
    sku = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return "Product: {}".format(self.name)