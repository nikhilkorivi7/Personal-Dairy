"""
URL configuration for Daily_Diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from DiaryAPP.views import Register,Login,Writing,ShowRecords,base,view_page,home,contact,Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',Register.as_view(),name='reg'),
    path('login',Login.as_view(),name='log'),
    path('writing',Writing.as_view(),name='write'),
    path('showrecs',ShowRecords.as_view(),name='recs'),
    path('base',base.as_view(),name='base'),
    path('view',view_page.as_view(),name='view'),
    path('home',home.as_view(),name='home'),
    path('contact',contact.as_view(),name='contact'),
    path('logout', Logout, name='logout')
]
