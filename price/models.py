from django.db import models

# Create your models here.


class Items(models.Model):
    isbn_id = models.IntegerField(primary_key=True)
    isbn = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    image = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    discount = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    publisher = models.CharField(max_length=100)
    pubdate = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=1000, null=True)
    searchDate = models.DateField(null=True)

    def __str__(self):
        return str(self.isbn_id)

    class Meta:
        db_table = 'items'


#class Items(models.Model):
#    title = models.CharField(max_length=100)
#    link = models.CharField(max_length=100)
#    image = models.CharField(max_length=100, null=True)
#    lprice = models.DecimalField(max_digits=8, decimal_places=2, null=True)
#    hprice = models.DecimalField(max_digits=8, decimal_places=2, null=True)
#    mallName = models.CharField(max_length=100)
#    productId = models.IntegerField(primary_key=True)
#    productType = models.DecimalField(max_digits=8, decimal_places=2, null=True)
#    searchDate = models.DateField(null=True)
#
#   def __str__(self):
#        return str(self.productId)
#
#    class Meta:
#        db_table = 'items'

