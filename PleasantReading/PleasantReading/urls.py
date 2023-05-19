"""
URL configuration for PleasantReading project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from PleasantReading import settings
from api import userApi
from api.userApi import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', my_view, name='upload'),  # 添加上传图片的路由
    path('login', userApi.login),
    path('register', userApi.register),
    path('submit/', userApi.my_view),
    path('gallery/', userApi.image_gallery),
    path('changepwd', userApi.changePwd),
    path('changeinfo', userApi.changeInfo),
    path('getinfo', userApi.getInfo),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)