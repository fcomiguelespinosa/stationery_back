from django.db import models
from ..items.models import Item

class Sale(models.Model):
    sale = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    
    class Meta:
        db_table = 'sale'