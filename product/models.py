from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

class Category(models.Model):
	name 		= models.CharField(max_length=100, unique=True)
	pic 		= models.ImageField(upload_to="{}/".format(name), blank=True, null=True)
	slug 		= models.SlugField(max_length=100, blank=True, null=True, unique=True)
	desc 		= RichTextField(blank=True)

	def __str__(self):
		return str(self.name)

class SubCategory(models.Model):
	category 	= models.ForeignKey(Category, on_delete=models.PROTECT)
	name 		= models.CharField(max_length=100)
	pic 		= models.ImageField(upload_to="{}/{}/".format(category.name, name))
	slug 		= models.SlugField(max_length=100, blank=True, null=True, unique=True)
	desc 		= RichTextField(blank=True)

	def __str__(self):
		return str(self.name) + " - " + self.category.__str__()

	def get_absolute_url(self):
		return reverse("product:shop", kwargs={'subCategorySlug': self.slug})


class Prod(models.Model):
	subCategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)

	name 		= models.CharField(max_length=100)
	desc 		= RichTextField(blank=True, null=True)
	detail 		= RichTextField(null=True)
	origPrice	= models.FloatField(blank=True, null=True)
	price 		= models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	discount 	= models.DecimalField(default=10.00, max_digits=6, decimal_places=2)
	status 		= models.CharField(max_length=50, default="New")

	hotDeal 	= models.BooleanField(default=False)
	special 	= models.BooleanField(default=False)
	inStock 	= models.BooleanField(default=True)

	timestamp 	= models.DateTimeField(auto_now_add=True)
	slug 		= models.SlugField(max_length=500)

	keywords 	= RichTextField(blank=True, null=True)

	def __str__(self):
		return str(self.name) + " - " + self.subCategory.__str__() + " - instock = " + str(self.inStock)

	def get_absolute_url(self):
		return reverse("product:prod", kwargs={'prodSlug': self.slug})


class ProdMedia(models.Model):
	prod 	= models.ForeignKey(Prod, on_delete=models.CASCADE)
	pic 	= models.ImageField(upload_to='{}/'.format(prod.name)) # If possible upload to its repective folder

	def __str__(self):
		return self.prod.__str__()

class RequestProd(models.Model):
	name 		= models.CharField(max_length=100)
	phoneNumber = models.IntegerField(blank=True, null=True)