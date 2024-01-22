from django.db import models

# Create your models here.
class customer(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=180 ,blank=False, default='')
    lastname=models.CharField(max_length=180 ,blank=False, default='')
    email=models.CharField(max_length=180 ,blank=False, default='')
    username=models.CharField(max_length=180 ,blank=False, unique=True)
    password=models.CharField(max_length=180 ,blank=False, unique=True)

    class Meta:
        db_table='customer_details'