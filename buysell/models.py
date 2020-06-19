from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    cost=models.DecimalField(decimal_places=2, max_digits=7)
    pass

class Cart(models.Model):
    items=models.ManyToManyField('item')
    username=models.OneToOneField('User')
    total_cost=models.DecimalField(decimal_places=2, max_digits=9)
    pass
