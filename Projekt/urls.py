"""Projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from system_rezerwacyjny import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new', views.new_room, name="new_room"),
    path('room/modify/<int:id>', views.modify_room, name="modify_room"),
    path('room/delete/<int:id>', views.delete_room, name="delete_room"),
    path('room/<int:id>', views.single_room, name="single_room"),
    path('room/all/', views.all_rooms, name="all_rooms"),
    path('reservation/<int:id>/', views.reservation, name="reservation"),
    path('search', views.search, name="search"),
]
