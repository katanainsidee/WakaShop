from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=255)
    clothing_type = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', args=[str(self.slug)])

    def __str__(self):
        return self.name

    def get_images(self):
        return self.productimage_set.all()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main/product_images/')

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"