from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='channel-search'),
    path('<str:room_name>/', views.room, name='room'),
]