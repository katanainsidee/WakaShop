from django.contrib import admin

from .models import Product, ProductImage

'''
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'count')
    search_fields = ('name', 'description', 'price', 'count')
'''


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    list_display = ('name', 'brand', 'sex', 'description', 'price', 'display_images', 'clothing_type')

    def display_images(self, obj):
        return ', '.join([str(image) for image in obj.get_images()])

    display_images.short_description = 'Images'


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
