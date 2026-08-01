from django.contrib import admin
from .models import *
import subprocess
import sys


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'file']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'category', 'brand', 'price', 'inventory']
    list_filter = ['category', 'brand']
    inlines = [ImageInline]

    def save_model(self, request, obj, form, change):

        super().save_model(request, obj, form, change)

        subprocess.Popen(
            [sys.executable, "rag/update_vectorstore.py"]
        )