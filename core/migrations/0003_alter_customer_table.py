# Generated by Django 5.0 on 2024-02-01 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_customer_email'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='users',
        ),
    ]
