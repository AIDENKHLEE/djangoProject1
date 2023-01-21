"""djangoProject1 URL Configuration

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
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home', views.home, name='home'),
    # path('home', views.home, name='home1'),
    path('',views.view_attributes,name='home'),
   # path('maintenance',views.maintenance,name='maintenance'),
    path('match', views.match, name= 'match'),
    path('registration/register',views.register_new_user,name='register_user'),
   # path('map',views.map,name="map"),
    path('match/', views.confirm_match, name='confirm_match'),
]

