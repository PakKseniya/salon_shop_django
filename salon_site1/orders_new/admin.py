from django.contrib import admin
from .models import OrderNew, OrderNewItem


class OrderItemInline(admin.TabularInline):
    model = OrderNewItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'telephone', 'status', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    search_fields = ['id']
    inlines = [OrderItemInline]


admin.site.register(OrderNew, OrderAdmin)
