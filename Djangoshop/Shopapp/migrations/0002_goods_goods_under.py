# Generated by Django 2.2.1 on 2019-07-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_under',
            field=models.IntegerField(default=1, verbose_name='商品状态'),
        ),
    ]