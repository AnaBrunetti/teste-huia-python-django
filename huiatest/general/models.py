from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# https://docs.djangoproject.com/en/3.1/topics/db/models/

class Client(models.Model):

    name = models.CharField("Name", max_length=255)
    cpf = models.CharField("CPF", max_length=11)
    birth_date = models.DateField("Birth Date")
    inactive = models.BooleanField("Inactive", default=False)

    class Meta:

        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f"{self.name}"


class QualityLot(models.Model):

    fabrication_date = models.DateField("Fabrication Date")
    quality = models.IntegerField("Quantity")
    inactive = models.BooleanField("Inactive", default=False)

    class Meta:

        db_table = 'quality_lot'
        verbose_name = 'Quality Lot'
        verbose_name_plural = 'Quality Lots'

    def __str__(self):
        return f"Quality Lot Id: {self.id}"



class Product(models.Model):

    name = models.CharField("Name", max_length=255)
    description = models.TextField("Description")
    quality_lot = models.ForeignKey("general.QualityLot", verbose_name="Quality Lot", on_delete=models.PROTECT, limit_choices_to={'inactive' : False})
    color = models.CharField("Color", max_length=255)
    price = models.DecimalField("Price", max_digits=11, decimal_places=2)
    inactive = models.BooleanField("Inactive", default=False)

    class Meta:

        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"Product: {self.name} - Price: {self.price}"


class Order(models.Model):

    client = models.ForeignKey("general.Client", verbose_name="Client", on_delete=models.PROTECT, limit_choices_to={'inactive' : False})
    seller = models.ForeignKey(User, verbose_name="Seller", on_delete=models.PROTECT, limit_choices_to={'is_active' : True})
    products = models.ManyToManyField("general.Product", verbose_name="Products", limit_choices_to={'inactive' : False})
    purchase_date = models.DateField(auto_now=True)
    inactive = models.BooleanField("Inactive", default=False)
    total_value = models.DecimalField("Total Value", max_digits=11, decimal_places=2)
    
    class Meta:

        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order Id: {self.id} - Client: {self.client}"        
