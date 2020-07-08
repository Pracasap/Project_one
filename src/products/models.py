from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title		= models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	price		= models.DecimalField(max_digits=10000, decimal_places=2)
	summary		= models.TextField()
	featured 	= models.BooleanField(default=True)

	# def get_absolute_url(self):
	# 	return f"/products/{self.id}/"

	def get_absolute_url(self):
		return reverse("products:product-detail", kwargs={"id": self.id})