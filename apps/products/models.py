from django.db import models
from cloudinary.models import CloudinaryField
from apps.categories.models import Category
from HIVE_BACKEND.constants import PRODUCT_TYPE

# Create your models here.
class Product(models.Model):
    class Meta(object):
        db_table = 'product'

    name = models.CharField(
        'Name', max_length=60, null=False, blank=False
    )
    description = models.CharField(
        'Description', max_length=255, null=True,blank=True
    )
    price = models.FloatField(
        'Price', null=False, blank=False
    )
    image = CloudinaryField(
        'Product Image', blank=True, null=True
    )
    type = models.CharField(
        'Type',max_length=60, null=False, blank=False, choices=PRODUCT_TYPE
    )
    category = models.ForeignKey(
        Category, related_name='related_category', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
