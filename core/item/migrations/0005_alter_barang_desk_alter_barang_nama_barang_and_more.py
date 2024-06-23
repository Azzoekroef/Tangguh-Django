# Generated by Django 5.0.2 on 2024-06-22 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_alter_barang_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='desk',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='barang',
            name='nama_barang',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='barang',
            name='point',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='barang',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='item.statusbarang'),
        ),
    ]