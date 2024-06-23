from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import News
# from .serializers import
# from utils.custome_response import CustomResponse
from django.contrib.auth import login as lo
from django.conf import settings
from django.contrib.auth.hashers import make_password
from datetime import timedelta
import datetime
import pytz
from django.utils import timezone
# Create your views here.
User = get_user_model()

@api_view(['GET'])
@permission_classes([AllowAny])
def donate_option(request):
    news = News.objects.filter(status=True)
    news_data = []
    for new in news:
        new_data = {
            "id": new.id,
            "title": new.nama,
        }
        news_data.append(new_data)
    return Response({
        "data" : news_data
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def get_news_donate(request):
    news = News.objects.filter(status=True)
    news_data = []
    for new in news:
        base_url = settings.BASE_URL
        date_new = new.date_modified
        diff_time = format_time_ago(date_new)
        if new.image_news:
            image_url = f"{base_url}{new.image_news.url}"
        else:
            image_url = f"{base_url}/media/news/Screenshot1.png" # gambar default
        new_data = {
            "id": new.id,
            "title": new.nama,
            "image_new": image_url,
            "lokasi": new.lokasi,
        }
        news_data.append(new_data)
    return Response({
        "data" : news_data
    })
    
@api_view(['GET'])
@permission_classes([AllowAny])
def getNews(request):
    news = News.objects.all()
    news_data = []
    for new in news:
        base_url = settings.BASE_URL
        date_new = new.date_modified
        diff_time = format_time_ago(date_new)
        if new.image_news:
            image_url = f"{base_url}{new.image_news.url}"
        else:
            image_url = f"{base_url}/media/news/Screenshot1.png" # gambar default
        new_data = {
            "id": new.id,
            "title": new.nama,
            "image_new": image_url,
            "deskripsi": new.desk,
            "date": diff_time
        }
        news_data.append(new_data)
    return Response({
        "data" : news_data
    })
        # return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_news_by_id(request,id):
    news = News.objects.get(id=id)
    date_new = news.date_modified
    diff_time = format_time_ago(date_new)
    base_url = settings.BASE_URL
    if news.image_news:
        image_url = f"{base_url}{news.image_news.url}"
    else:
        image_url = f"{base_url}/media/news/Screenshot1.png"
    return Response({
        "id": news.id,
        "title": news.nama,
        "image_news": image_url,
        "deskripsi": news.desk,
        "date": diff_time
        })



def format_time_ago(post_time):
    now = timezone.now()
    print(now)
    print(post_time)
    time_diff = now - post_time

    if time_diff < timedelta(minutes=1):
        return f"{time_diff.seconds} detik yang lalu"
    elif time_diff < timedelta(hours=1):
        return f"{time_diff.seconds // 60} menit yang lalu"
    elif time_diff < timedelta(days=1):
        return f"{time_diff.seconds // 3600} jam yang lalu"
    elif time_diff < timedelta(days=30):
        return f"{time_diff.days} hari yang lalu"
    elif time_diff < timedelta(days=365):
        months = int(time_diff.days / 30)
        return f"{months} bulan yang lalu"
    else:
        years = int(time_diff.days / 365)
        return f"{years} tahun yang lalu"
