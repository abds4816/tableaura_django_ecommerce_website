from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='categories/%Y/%m/%d')

    def __str__(self):
        return self.category_name

class Product(models.Model):

    DEMONSIONS = (
        ('sm', '25x40cm'),
        ('md', '40x70cm'),
        ('lg', '80x120cm')
    )

    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    sm_price = models.DecimalField(max_digits=8, decimal_places=2)
    sm_old_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    md_price = models.DecimalField(max_digits=8, decimal_places=2)
    md_old_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    lg_price = models.DecimalField(max_digits=8, decimal_places=2)
    lg_old_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    demonsions = models.CharField(max_length=2, choices=DEMONSIONS, null=True, blank=True)
    views = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    publish_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name