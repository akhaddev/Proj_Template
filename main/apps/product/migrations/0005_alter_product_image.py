# Generated by Django 4.1.5 on 2024-09-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/.2024-09-16.18-34-12'),
        ),
    ]
