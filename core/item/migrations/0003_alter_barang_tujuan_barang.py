# Generated by Django 5.0.2 on 2024-06-22 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_barang_date_barang_date_modified'),
        ('news', '0003_alter_news_desk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='tujuan_barang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.news'),
        ),
    ]
