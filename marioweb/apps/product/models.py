from django.db import models

# Create your models here.


class Product(models.Model):
    description = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    class Meta:
        db_table = 'product'
		