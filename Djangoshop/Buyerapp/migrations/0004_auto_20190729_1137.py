# Generated by Django 2.2.1 on 2019-07-29 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Buyerapp', '0003_order_orderdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='Goods_id',
            new_name='goods_id',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='Goods_name',
            new_name='goods_name',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='Goods_number',
            new_name='goods_number',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='Goods_price',
            new_name='goods_price',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='Goods_store',
            new_name='goods_store',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='Goods_total',
            new_name='goods_total',
        ),
    ]
