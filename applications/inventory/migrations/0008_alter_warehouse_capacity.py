# Generated by Django 4.2.16 on 2024-11-26 07:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_warehouse_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='capacity',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
