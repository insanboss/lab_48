from django.db import models

# Create your models here.
category_choices = [('food', 'еда'), ('household_products', 'бытовые товары'), ('garden_staff', 'товары для огорода'), ('other', 'разное')]


class Product(models.Model):
    product = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание товара')
    categories = models.CharField(max_length=50, null=False, blank=False, choices=category_choices, default='other', verbose_name='категория')
    remainder = models.PositiveIntegerField(verbose_name='остаток')
    cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='стоимость')

    def __str__(self):
        return "{}. {}".format(self.pk, self.product)
