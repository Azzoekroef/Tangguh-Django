from django.db import models
from django.utils import timezone
import pytz
import requests
# Create your models here.

class CategoryNews(models.Model):
    nama_category = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_category

class News(models.Model):
    nama = models.CharField(max_length=100)
    image_news = models.ImageField(upload_to='news/')
    desk = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey(CategoryNews, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    lokasi = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Mendapatkan waktu saat ini dalam UTC
        now_utc = timezone.now()
        
        # Mendapatkan zona waktu lokal dari internet
        response = requests.get("http://worldtimeapi.org/api/ip")
        data = response.json()
        timezone_str = data['timezone']
        
        # Mengubah waktu UTC ke zona waktu lokal
        local_tz = pytz.timezone(timezone_str)
        now_local = now_utc.astimezone(local_tz)
        self.date = now_local
        # Menggunakan waktu lokal untuk date_modified
        self.date_modified = now_local
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama