# Generated by Django 5.0 on 2024-01-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(default='', max_length=180)),
                ('lastname', models.CharField(default='', max_length=180)),
                ('email', models.CharField(default='', max_length=180)),
                ('username', models.CharField(max_length=180, unique=True)),
                ('password', models.CharField(max_length=180, unique=True)),
            ],
            options={
                'db_table': 'customer_details',
            },
        ),
    ]
