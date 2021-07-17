from django.contrib import admin
from  .models import Restaurant,Food,Order,Comment
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Comment)
