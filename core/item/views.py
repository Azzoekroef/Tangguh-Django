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
import re
from .models import CustomUser
from .models import Barang, CategoryBarang, StatusBarang
# from .serializers import
# from utils.custome_response import CustomResponse
from django.contrib.auth import login as lo
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import pytz
from datetime import datetime
import requests
# Create your views here.
User = get_user_model()
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def option_category(request):
    categorys = CategoryBarang.objects.all()
    datas = []
    for category in categorys:
        data = {
            "id": category.id,
            "name": category.nama_category,
        }
    datas.append(data)
    return Response({
        "data": datas
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_item(request):
    pattern = r'cache/([^/]+)$'
    response = requests.get("http://worldtimeapi.org/api/ip")
    date_barang = timezone.now()
    data = response.json()
    timezone_str = data['timezone']
    local_tz = pytz.timezone(timezone_str)
    now_local = date_barang.astimezone(local_tz)
    formatted_time = now_local.strftime("%d-%m-%Y %H:%M")

    print(date_barang)
    user = request.user
    # nama_barang = request.data('nama_barang')
    image = request.data.get('image')  # Menggunakan .get() untuk mengakses data dari request.data
    desk = request.data.get('deskripsi')
    category = request.data.get('category')
    tujuan = request.data.get('tujuan')
    image = re.search(pattern, image)
    result = 'barang/' + image.group(1)
    if image and desk and category and tujuan:
        category = CategoryBarang.objects.get(nama_category=category.lower()) # Ambil objek Category berdasarkan ID
        tujuan = News.objects.get(nama=tujuan) # Ambil objek News berdasarkan ID
        date_barang = timezone.now()
        print(date_barang)
        barang = Barang.objects.create(
            customuser=user,
            image_barang=result,
            desk=desk,
            category=category,
            tujuan_barang=tujuan
        )
        return Response({
            'date': formatted_time,
            'lokasi_posko': "Padang Center",
            'message': "Berhasil"

        }, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Incomplete data provided'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_item_list_user(request):
    user = request.user
    barangs = Barang.objects.filter(customuser=user.id)
    news_data = []
    for barang in barangs:
        category = CategoryBarang.objects.get(id=barang.category.id)
        status_item = StatusBarang.objects.get(id=barang.status.id)
        new_data = {
            "id": barang.id,
            "category": category.nama_category,
            "status": status_item.nama_status,
        }
        news_data.append(new_data)
    total_donasi = len(news_data)
    
    return Response({
        "total_donasi": total_donasi,
        "data" : news_data
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_total_item_user(request):
    user = request.user
    barangs = Barang.objects.filter(customuser=user.id)
    total_donasi = len(barangs)
    
    return Response({
        "total_donasi": total_donasi,
    })