# Generated by Django 5.0 on 2023-12-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sex',
            field=models.CharField(default='Мужское', max_length=255),
            preserve_default=False,
        ),
    ]
