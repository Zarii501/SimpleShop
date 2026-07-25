from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام ویژگی')

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='دسته‌بندی')
    name = models.CharField(max_length=128, verbose_name='نام')
    brand = models.CharField(max_length=128, verbose_name='برند')
    price = models.PositiveBigIntegerField(default=0, verbose_name='قیمت')
    inventory = models.PositiveBigIntegerField(default=0, verbose_name='موجودی')
    connectionـtype = models.CharField(max_length=255, verbose_name='نوع اتصال')
    color = models.CharField(max_length=128, verbose_name='رنگ')
    warranty = models.CharField(max_length=128, verbose_name='گارانتی')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        ordering = ['-name']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),
        ]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def __str__(self):
        return self.name
    


class Image(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE, verbose_name="محصول")
    file = models.ImageField(upload_to="product_images/%Y/%m/%d")
    
    verbose_name="تصویر"
    verbose_name_plural="تصاویر"