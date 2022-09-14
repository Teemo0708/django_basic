"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import index, welcome, template_test

urlpatterns = [

    # path('주소', 뷰, 주소의 별명)
    path('admin/', admin.site.urls),
    path('welcome/', welcome),
    path('test/', template_test),
    path('', index), #위에서 매칭된 뷰가 없을 경우 이쪽으로 연결되기 때문에 맨 아래에 위치하는것이 좋음
]
