# Generated by Django 2.2.1 on 2019-07-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyerapp', '0005_auto_20190729_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(default=1, verbose_name='订单状态'),
        ),
    ]