from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):

	product_name = models.CharField('Produit', max_length=200, unique = True)
	slug = models.SlugField('slug' ,max_length=200, unique=True)
	description = models.TextField(max_length=500, blank=True)
	price = models.FloatField('Prix', default=0.0)
	images = models.ImageField(upload_to='photos/products') 
	stock =models.IntegerField(default=0)
	is_available = models.BooleanField('Disponible ?' ,default=True)
	categorie = models.ForeignKey(Category, on_delete = models.CASCADE)
	created_date =models.DateTimeField('Date de creation' ,auto_now_add=True)
	modified_date = models.DateTimeField('Date de modification', auto_now=True)

	class Meta:
		verbose_name = 'Produit'
		verbose_name_plural = 'Produits'


	def get_url(self):
		return reverse('product_detail', args=[self.categorie.slug, self.slug])



	def __str__(self):
		return self.product_name
