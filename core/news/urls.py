from django.urls import path
from . import views


urlpatterns = [
    path('donate/', views.get_news_donate, name='news'),
    path('new/', views.getNews, name='news'),
    path('donate_option/', views.donate_option, name='news'),
    path('get_news/<int:id>/', views.get_news_by_id, name='news'),
]