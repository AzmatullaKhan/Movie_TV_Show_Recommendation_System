from django.contrib import admin

# Register your models here.
from .models import customer
from .models import watchList

admin.site.register(customer)
admin.site.register(watchList)