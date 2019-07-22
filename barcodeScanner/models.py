from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=2048)
    # Not sure what max length should be, 8 is tentative
    plu = models.CharField(primary_key=True, max_length=8)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=2048)
    # Not sure what max length should be, 8 is tentative
    vendorId = models.CharField(primary_key=True, max_length=8)

    def __str__(self):
        return self.name
