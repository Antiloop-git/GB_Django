# Generated by Django 3.2.3 on 2021-06-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210617_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='удалена'),
        ),
    ]