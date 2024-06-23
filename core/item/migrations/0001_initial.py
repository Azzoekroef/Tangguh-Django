# Generated by Django 5.0.2 on 2024-06-22 04:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryBarang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusBarang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=100)),
                ('image_barang', models.ImageField(upload_to='barang/')),
                ('desk', models.TextField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('point', models.IntegerField()),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tujuan_barang', models.ForeignKey(blank=True, default='empty', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='news.news')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.statusbarang')),
            ],
        ),
    ]