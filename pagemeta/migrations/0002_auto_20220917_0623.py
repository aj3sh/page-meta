# Generated by Django 2.2.28 on 2022-09-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagemeta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metaforpage',
            name='image',
            field=models.ImageField(upload_to='page-meta/', verbose_name='Image'),
        ),
    ]
