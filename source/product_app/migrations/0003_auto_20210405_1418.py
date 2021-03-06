# Generated by Django 3.1.7 on 2021-04-05 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_basket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='количество продуктов в заказе')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrderProduct', to='product_app.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductOrder', to='product_app.product', verbose_name='продукт')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='orders', through='product_app.ProductOrder', to='product_app.Product'),
        ),
    ]
