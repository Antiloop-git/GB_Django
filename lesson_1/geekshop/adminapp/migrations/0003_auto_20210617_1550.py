# Generated by Django 3.2.3 on 2021-06-17 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_productcategory_is_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='is_delete',
        ),
    ]
