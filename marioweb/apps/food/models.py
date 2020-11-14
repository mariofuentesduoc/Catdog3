from django.db import models

# Create your models here.

class Food(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    class Meta:
        db_table = 'food'