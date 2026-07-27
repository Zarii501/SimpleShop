from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام ویژگی')
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='دسته‌بندی')
    name = models.CharField(max_length=128, verbose_name='نام')
    slug = models.SlugField(max_length=255, verbose_name='اسلاگ')
    brand = models.CharField(max_length=128, verbose_name='برند')
    price = models.PositiveBigIntegerField(default=0, verbose_name='قیمت')
    inventory = models.PositiveBigIntegerField(default=0, verbose_name='موجودی')
    connectiontype = models.CharField(max_length=255, verbose_name='نوع اتصال')
    color = models.CharField(max_length=128, verbose_name='رنگ')
    warranty = models.CharField(max_length=128, verbose_name='گارانتی')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        ordering = ['-name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
        ]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('products:product_detail', args=[self.id, self.slug])
    


class Image(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE, verbose_name="محصول")
    file = models.ImageField(upload_to="product_images/%Y/%m/%d")

    class Meta:    
        verbose_name="تصویر"
        verbose_name_plural="تصاویر"
