from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'departure', 'arrival', 'date', 'order_status')
    list_editable = ('order_status',)
    list_filter = ('departure', 'arrival', 'date', 'created_at', 'order_status')

admin.site.register(Order, OrderAdmin)