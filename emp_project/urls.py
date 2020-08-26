"""emp_project URL Configuration

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
from django.urls import path
from emp_register import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/', views.emp),
    path('view/', views.view),
    path('delete/<id>', views.delete),
    path('edit/<id>', views.edit),
    path('add/', views.add),
    path('update/<id>', views.update),  
    url(r'^search/', views.search, name="search"),
]

