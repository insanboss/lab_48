from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
category_choices = [('food', 'еда'), ('household_products', 'бытовые товары'), ('garden_staff', 'товары для огорода'),
                    ('other', 'разное')]


class Product(models.Model):
    product = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание товара')
    categories = models.CharField(max_length=50, null=False, blank=False, choices=category_choices, default='other',
                                  verbose_name='категория')
    remainder = models.PositiveIntegerField(verbose_name='остаток')
    cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='стоимость')

    def __str__(self):
        return "{}. {}".format(self.pk, self.product)


class Basket(models.Model):
    product = models.ForeignKey("product_app.Product", on_delete=models.CASCADE, related_name='basket',
                                verbose_name='продукт')
    quantity = models.IntegerField(verbose_name='количество продуктов в корзине')

    def get_total(self):
        return self.quantity * self.product.cost

    def __str__(self):
        return "{}. {}".format(self.pk, self.quantity)


class Order(models.Model):
    user_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField('product_app.Product', related_name='orders', through='product_app.ProductOrder',
                                  through_fields=('order', 'product'))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='Order', verbose_name='user',
                             null=True, blank=True)

    def total(self):
        total = 0

        for product in self.OrderProduct.all():
            total += product.get_total()

        return total

    def __str__(self):
        return "{}. {}".format(self.created_at, self.user_name)


class ProductOrder(models.Model):
    product = models.ForeignKey("product_app.Product", on_delete=models.CASCADE, related_name='ProductOrder',
                                verbose_name='продукт')
    order = models.ForeignKey("product_app.Order", on_delete=models.CASCADE, related_name='OrderProduct',
                                verbose_name='Заказ')
    quantity = models.IntegerField(verbose_name='количество продуктов в заказе')

    def get_total(self):
        return self.quantity * self.product.cost



    def __str__(self):
        return "{}. {}".format(self.order, self.product)
