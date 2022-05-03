from django.db import models


# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    order = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = u'Brand'
        verbose_name_plural = u'Brands'

    def __str__(self):
        return self.title


class Product(models.Model):
    sku = models.CharField('Sku', max_length=50, unique=True)
    name = models.CharField('Name', max_length=120)
    price = models.FloatField('Price')
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)
    is_active = models.BooleanField('Is active?', default=True)
    order_by = models.SmallIntegerField('Order', default=0)

    class Meta:
        ordering = ['order_by', 'is_active', 'name', 'brand_id']
        verbose_name = u'Product'
        verbose_name_plural = u'Products'

    def __str__(self):
        return self.name


class TrackProduct(models.Model):
    user = models.CharField('User', max_length=50)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    date = models.DateTimeField('Date', auto_now_add=True)

    @staticmethod
    def create_track(user, product_id):
        product = Product.objects.get(pk=product_id)
        TrackProduct.objects.create(user=user, product=product)
