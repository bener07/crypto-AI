from django.contrib import admin
from database.models import coins, test_model
# Register your models here.

admin.site.register(coins)
admin.site.register(test_model)
