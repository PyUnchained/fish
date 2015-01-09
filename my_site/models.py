from django.contrib import admin
from django.db import models

# Create your models here.
class ProductItem(models.Model):

	name = models.CharField(max_length = 100)
	price = models.DecimalField(max_digits = 6, decimal_places = 2)

	is_available = models.BooleanField(default = True)
	can_deliver = models.BooleanField(default = True)

	class Admin():
		pass

class Order(models.Model):
	product = models.ForeignKey(ProductItem)
	price = models.DecimalField(max_digits = 6, decimal_places = 2)
	days = models.CharField(max_length = 10)
	date = models.DateField()
	frequency = models.CharField(max_length = 2)
	duration = models.IntegerField()
	address_street = models.CharField(max_length = 100)
	quantity = models.IntegerField()
	num = models.CharField(max_length = 20)

	delivered = models.BooleanField(default = False)

	class Admin():
		pass


admin.site.register(ProductItem)
admin.site.register(Order)