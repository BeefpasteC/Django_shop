# Generated by Django 2.2.1 on 2019-07-29 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buyerapp', '0004_auto_20190729_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Buyerapp.Address', verbose_name='订单地址'),
        ),
    ]