# Generated by Django 5.0.2 on 2024-06-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_date_news_date_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='desk',
            field=models.TextField(),
        ),
    ]