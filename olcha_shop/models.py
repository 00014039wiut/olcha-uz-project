from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/category')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Group(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/group')

    def __str__(self):
        return self.name


class Key(models.Model):
    key_name = models.CharField(max_length=100)

    def __str__(self):
        return self.key_name


class Value(models.Model):
    value_name = models.CharField(max_length=100)

    def __str__(self):
        return self.value_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.FloatField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    value = models.ForeignKey(Value, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Attributes'

    def __str__(self):
        return self.product.name


class Image(models.Model):
    image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='products')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.image_name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    content = models.TextField()
    file = models.FileField(upload_to='comment_files/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
