from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    supplier_code = models.CharField(max_length=20, blank=True)
    buying_price = models.DecimalField(max_digits=12, decimal_places=2)
    selling_price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'item'