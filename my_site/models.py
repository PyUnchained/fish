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


admin.site.register(ProductItem)