from django.contrib import admin
from delivering.models import *


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('field',)

    prepopulated_fields = {"slug": ("field",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'producer', 'status', 'description', 'old_price', 'price')

    fieldsets = (
        ('Information of a product', {
            'fields': ('category', 'image', 'name', 'producer', 'status', 'description', 'old_price', 'price')
        }),
        ('Slug', {
            'classes': ('collapse',),
            'fields': ('slug',)
        })
    )

    prepopulated_fields = {"slug": ("category", "name", 'producer', 'status', 'price')}


@admin.register(SelectedProduct)
class SelectedProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'producer', 'price', 'total_price')

    fieldsets = (
        ('Information of a product', {
            'fields': ('product', 'unit_id', 'image', 'name', 'description', 'producer', 'number', 'price', 'total_price')
        }),
    )


class BoughtProductAdmin(admin.TabularInline):
    model = BoughtProduct

    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'email', 'telephone', 'total_price', 'data', 'status')

    fieldsets = (
        ('Information about the user', {
            'fields': ('name', 'last_name', 'sure_name', 'telephone', 'email', 'wish')
        }),
        ('Information about the order', {
            'fields': ('area', 'city', 'department', 'total_price', 'data', 'status')
        })
    )

    inlines = [BoughtProductAdmin]


@admin.register(BoughtProduct)
class BoughtProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'number', 'price', 'total_price')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'mark', 'name', 'email', 'text', 'data', 'audit')
