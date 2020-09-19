"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from boards import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),


    path('board/create/', views.BoardCreate.as_view(), name='board-create'),
    path('board/list/', views.BoardsList.as_view(), name='board-list'),
    path('board/<int:board_id>/delete/', views.BoardDelete.as_view(), name='board-delete'),
    path('board/<int:board_id>/detail/', views.BoardDetail.as_view(), name='board-detail'),

    path('task/<int:board_id>/add/', views.TaskAdd.as_view(), name='task-add'),
    path('task/<int:board_id>/<int:task_id>/update/', views.TaskUpdate.as_view(), name='task-update'),
    path('task/<int:board_id>/<int:task_id>/delete/', views.TaskDelete.as_view(), name='task-delete'),
    
]
