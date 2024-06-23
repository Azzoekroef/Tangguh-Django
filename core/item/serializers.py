from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Barang, CategoryBarang
from django.conf import settings
from django.contrib.auth import get_user_model

class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = ('username', 'email', 'image')
                  
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = ('customuser', 'image_barang', 'desk', 'category', 'tujuan_barang')

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     super().__init__(*args, **kwargs)

    # def create(self, validated_data):
    #     # Tambahkan user ke validated_data
    #     if self.user is not None:
    #         validated_data['user'] = self.user
    #     return super().create(validated_data)

    # def create(self, validated_data):
    #     item = Barang.objects.create(
    #         customuser=validated_data['user'],
    #         image_barang=validated_data['image'],
    #         desk=validated_data['desk'],
    #         category=validated_data['category'],
    #         tujuan_barang=validated_data['tujuan'],  
    #     )
    #     return item