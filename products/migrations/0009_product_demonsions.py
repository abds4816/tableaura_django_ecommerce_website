# Generated by Django 3.2.7 on 2021-10-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='demonsions',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]