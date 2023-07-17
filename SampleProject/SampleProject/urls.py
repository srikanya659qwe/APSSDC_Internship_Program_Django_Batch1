"""SampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from SampleApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('temp/',views.temp,name='temp'),
    path('dyn/<int:id>/<str:name>/',views.dynamic,name='dynamic'),
    path('inline/',views.inline,name='inline'),
    path('internal/',views.internal,name='internal'),
    path('external/',views.external,name='external'),

    path('boot/',views.boot,name='boot'),
    path('offline/',views.offline,name='offline'),

    path('reg/',views.reg,name='reg'),
    path('read/',views.read,name='read'),
    path('edit/<int:id>/',views.edit,name='edit'),


    path('email/',views.email,name='email'),
]
