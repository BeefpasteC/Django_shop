# Generated by Django 2.2.1 on 2019-07-30 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyerapp', '0006_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=32, verbose_name='商品名称')),
                ('goods_price', models.FloatField(verbose_name='商品价格')),
                ('goods_total', models.FloatField(verbose_name='商品总价')),
                ('goods_number', models.IntegerField(verbose_name='商品数量')),
                ('goods_picture', models.ImageField(upload_to='buyerapp/images', verbose_name='商品图片')),
                ('goods_id', models.IntegerField(verbose_name='商品id')),
                ('goods_store', models.IntegerField(verbose_name='商品店铺id')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
            ],
        ),
    ]
