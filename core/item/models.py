from django.db import models
from customuser.models import CustomUser
from news.models import News
# Create your models here.

class CategoryBarang(models.Model):
    nama_category = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_category

class StatusBarang(models.Model):
    nama_status = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_status

class Barang(models.Model):
    nama_barang = models.CharField(max_length=100, blank=True, null=True)
    image_barang = models.ImageField(upload_to='barang/')
    desk = models.TextField()
    category = models.ForeignKey(CategoryBarang, on_delete=models.CASCADE)
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusBarang, on_delete=models.CASCADE, default=1)
    tujuan_barang = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, blank=True)
    point = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.desk
