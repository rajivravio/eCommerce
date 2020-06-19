from django.db import models

class item(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    cost=models.DecimalField()
    pass

class cart(models.Model):
    items=models.ManyToManyField('item')
    total_cost=models.DecimalField()
    pass
