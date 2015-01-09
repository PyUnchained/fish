# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.DecimalField(max_digits=6, decimal_places=2)),
                ('days', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('frequency', models.CharField(max_length=2)),
                ('duration', models.IntegerField()),
                ('address_street', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('num', models.CharField(max_length=20)),
                ('delivered', models.BooleanField(default=False)),
                ('product', models.ForeignKey(to='my_site.ProductItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
