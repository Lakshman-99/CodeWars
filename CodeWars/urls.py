"""CodeWars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import sites
from django.urls import path, include
from django.views.generic import TemplateView
from codechallenge import views as v1

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('admin/', admin.site.urls),
    path('edi/',v1.editor,name='edi'),
    path('edi/runcode/',v1.code),
    path('index/',v1.index),
    path('account/', include('allauth.urls')),
    path('account/login/', v1.login, name="login"),
    path('account/signup/',v1.signup, name="signup"),
    path('practice/', v1.practice, name="practice"),
    #path('account/logout/',v1)
]
