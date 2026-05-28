from django.contrib import admin
from .models import Brand, Car, Message


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'brand',
        'model',
        'vehicle_type',
        'year',
        'price',
        'fuel_type',
        'transmission',
        'is_featured',
        'owner',
    )
    list_filter = ('brand', 'vehicle_type', 'fuel_type', 'transmission', 'year', 'is_featured')
    search_fields = ('title', 'model', 'description')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'receiver', 'car', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('subject', 'content')