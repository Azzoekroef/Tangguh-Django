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
from .models import CustomUser
from item.models import Barang
from .serializers import RegisterSerializer, CustomUserSerializer
# from utils.custome_response import CustomResponse
from django.contrib.auth import login as lo
from django.conf import settings
from django.contrib.auth.hashers import make_password
# Create your views here.
User = get_user_model()
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny,])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.filter(username=username).first()

    if user is None or not user.check_password(password):
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
    
    refresh = RefreshToken.for_user(user)
    lo(request, user)
    return Response({
        'refresh': str(refresh),
        'access' : str(refresh.access_token),
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def profile(request):
    user = User.objects.get(id=request.user.id)
    item = Barang.objects.filter(customuser=request.user.id)
    print(item)
    print(len(item))
    full_name = f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else None
    # address_parts = [part for part in [user.street_address, user.city, user.province] if part] 
    # address = ' '.join(address_parts) if address_parts else None
    # base_url = settings.BASE_URL
    # if user.image:
    #     image_url = f"{base_url}{user.image.url}"
    # else:
    #     image_url = f"{base_url}/media/image/Screenshot1.png" # gambar default
    return Response({
            "id": user.id,
            "username": user.username,
            "name": full_name,
            "email": user.email,
            # "image": image_url,
            # "mulai_bekerja": user.mulai_bekerja,
            "phone_number": user.phone_number,
            "point": user.point,
            # "address": address,
            # "jabatan" : user.jabatan.name,
            # "level_jabatan": user.level_jabatan.name
            })


@api_view(['GET'])
@permission_classes([AllowAny,])
def get_top_user(request):
    top_user = CustomUser.objects.all()[:3]
    base_url = settings.BASE_URL
    top_user_data = []
    for top in top_user:
        barang = Barang.objects.filter(customuser=top.id)
        for i in barang:
            top.point += i.point
        if top.image:
            image_url = f"{base_url}{top.image.url}"
        else:
            image_url = f"{base_url}/media/news/Screenshot1.png"
        fullname = f"{top.first_name} {top.last_name}"
        if top.is_hiden == True:
            fullname = "Anonymous"
            image_url = f"{base_url}/media/news/Screenshot1.png"
        data = {
            "id": top.id,
            "name": fullname,
            "image": image_url,
            "point": top.point,
        }
        top_user_data.append(data)
    top_user_data = sorted(top_user_data, key=lambda x: x["point"], reverse=True)
    return Response({
        "data": top_user_data,
    })
        
@api_view(['GET'])
@permission_classes([AllowAny,])
def get_top_user_50(request):
    top_user = CustomUser.objects.all()[:50]
    base_url = settings.BASE_URL
    top_user_data = []
    for top in top_user:
        barang = Barang.objects.filter(customuser=top.id)
        for i in barang:
            top.point += i.point
        if top.image:
            image_url = f"{base_url}{top.image.url}"
        else:
            image_url = f"{base_url}/media/news/Screenshot1.png"
        fullname = f"{top.first_name} {top.last_name}"
        if top.is_hiden == True:
            fullname = "Anonymous"
            image_url = f"{base_url}/media/news/Screenshot1.png"
        data = {
            "id": top.id,
            "name": fullname,
            "image": image_url,
            "point": top.point,
        }
        top_user_data.append(data)
    top_user_data = sorted(top_user_data, key=lambda x: x["point"], reverse=True)
    return Response({
        "data": top_user_data,
    })

@api_view(['PUT'])
@permission_classes([IsAuthenticated,])
def update_user(request):
    pass

            
    


