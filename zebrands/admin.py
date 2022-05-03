from django.contrib import admin
from zebrands.models import Brand, Product, TrackProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'brand_id', 'price', 'is_active')
    search_fields = ['sku', 'name', ]


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active')
    search_fields = ['title', 'description', ]


class TrackProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'date')
    search_fields = ['user', 'product', ]


admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(TrackProduct, TrackProductAdmin)
