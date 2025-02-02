# Generated by Django 4.2.16 on 2024-11-26 06:18

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_warehouse_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
