from django.db import models


class StockRecord(models.Model):
    product = models.ForeignKey('catalog.ProductItem', on_delete=models.CASCADE,related_name='stock_records')
    sku = models.CharField(max_length=50,null=True,blank=True,unique=True)
    buy_price = models.PositiveBigIntegerField(null=True,blank=True)
    sale_price = models.PositiveBigIntegerField(null=True,blank=True)
    num_stock = models.PositiveIntegerField(default=0)
    threshold_low_stack = models.PositiveIntegerField(null=True,blank=True)






