# Generated by Django 2.1.3 on 2019-03-19 03:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20190319_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='bounding_box',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True), blank=True, null=True, size=4),
        ),
        migrations.AlterField(
            model_name='map',
            name='center',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True), default=[0, 0], size=2),
        ),
    ]
