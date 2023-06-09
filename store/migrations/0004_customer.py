# Generated by Django 4.1.5 on 2023-03-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_category_alter_product_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=5)),
            ],
        ),
    ]
