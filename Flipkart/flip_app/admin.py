from django.contrib import admin
from flip_app.models import Category,Users,Products,Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Users)
admin.site.register(Order)
