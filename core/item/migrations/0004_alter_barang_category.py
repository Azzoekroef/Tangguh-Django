# Generated by Django 5.0.2 on 2024-06-22 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_barang_tujuan_barang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.categorybarang'),
        ),
    ]
