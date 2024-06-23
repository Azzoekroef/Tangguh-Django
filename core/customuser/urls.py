from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login,name='login'),
    path('profile/', views.profile, name='profile'),
    path('top_user/', views.get_top_user, name='top_user'),
    path('top_user_50/', views.get_top_user_50, name='top_user'),

]
