# Generated by Django 2.2.1 on 2019-07-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopapp', '0004_auto_20190725_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodstype',
            name='picture',
            field=models.ImageField(upload_to='store/images', verbose_name='类型图片'),
        ),
    ]
