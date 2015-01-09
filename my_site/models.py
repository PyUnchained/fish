#The admin module must be imported to register models with the admin.
from django.contrib import admin
from django.db import models

# Create your models here.
class ProductItem(models.Model):
	"""Represents a product item that the shop intends to sell"""

	name = models.CharField(max_length = 100)
	price = models.DecimalField(max_digits = 6, decimal_places = 2)

	is_available = models.BooleanField(default = True)
	can_deliver = models.BooleanField(default = True)

	#I've added this little section so that I can create, delete or
	#edit products in the built-in django admin manually.
	class Admin():
		pass

class Order(models.Model):
	"""Represents online orders from customers"""

	product = models.ForeignKey(ProductItem)
	total = models.DecimalField(max_digits = 6, decimal_places = 2)
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

#And here I've registered the models so they will actually be visible in
#the admin.
admin.site.register(ProductItem)
admin.site.register(Order)