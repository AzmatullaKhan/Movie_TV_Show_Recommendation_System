from django.db import models

# Create your models here.
class customer(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=180 ,blank=False, default='')
    lastname=models.CharField(max_length=180 ,blank=False, default='')
    email=models.CharField(max_length=180 ,blank=False, default='', unique=True)
    username=models.CharField(max_length=180 ,blank=False, unique=True)
    password=models.CharField(max_length=180 ,blank=False, unique=True)

    class Meta:
        db_table='customer_details'

class watchList(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=180 ,blank=False, default='')
    movie_id=models.CharField(max_length=180 ,blank=False, default='')
    genre=models.CharField(max_length=200 ,blank=False, default='')
    url=models.CharField(max_length=200 ,blank=False, default='')
    desc=models.CharField(max_length=800 ,blank=False, default='')
    director=models.CharField(max_length=200 ,blank=False, default='')
    writers=models.CharField(max_length=200 ,blank=False, default='')
    streaming=models.CharField(max_length=200 ,blank=False, default='')
    username=models.CharField(max_length=200 ,blank=False, default='', unique=False)    

    class Meta:
        db_table='watchlist_details'