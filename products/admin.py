from django.contrib import admin
from .models import Category, Product
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('is_active', 'category',)
    list_display = ('name', 'is_active',)
    search_fields = ('name',)

# admin.site.register(Category)
@admin.register(Category)
class CategoryImportExport(ImportExportModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)