from django.db import models


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    logo = models.ImageField(upload_to='bestbud/static/images')
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0,max_digits=5,decimal_places=2)
    def __str__(self):
        return self.name

class Purchase(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0,max_digits=5,decimal_places=2)
    date = models.DateTimeField('date purchased')
    qtd = models.IntegerField(default=1)
    total_price = models.DecimalField(default=0,max_digits=5,decimal_places=2)
    purchase_id = models.IntegerField(default=0)
    def __str__(self):
        return 'Compra ' + str(self.purchase_id)
