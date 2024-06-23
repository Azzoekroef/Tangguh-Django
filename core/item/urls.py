from django.urls import path
from . import views

urlpatterns = [
    path('item_option', views.option_category, name='item'),
    path('post_item/', views.post_item, name='item'),
    path('get_item_user/', views.get_item_list_user, name='item'),
    path('get_total_item_user/', views.get_total_item_user, name='item'),
]