# Generated by Django 4.2.6 on 2023-10-10 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_rename_items_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]