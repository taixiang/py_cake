# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0004_auto_20171022_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cake1',
            options={'ordering': ('pub_time',), 'verbose_name': '蛋糕详情', 'verbose_name_plural': '蛋糕详情'},
        ),
        migrations.RemoveField(
            model_name='cake1',
            name='category_id',
        ),
        migrations.AddField(
            model_name='cake1',
            name='category_id',
            field=models.ManyToManyField(related_name='cake_post', to='cake.Category'),
        ),
        migrations.AlterField(
            model_name='cake1',
            name='desc',
            field=models.CharField(max_length=500, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='cake1',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='优惠'),
        ),
        migrations.AlterField(
            model_name='cake1',
            name='img',
            field=models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='cake1',
            name='label',
            field=models.CharField(max_length=400, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='cake1',
            name='name',
            field=models.CharField(max_length=200, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='cake1',
            name='order',
            field=models.IntegerField(default=0, verbose_name='权重'),
        ),
        migrations.AlterField(
            model_name='cake1',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='价格'),
        ),
    ]
