"""
URL configuration for skillaid_connect_API project.

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
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title = 'Movie Review API',
        default_version = 'v1.0.0',
        description = 'The skillaid connect api allows users to learn from a variety of courses including tech, programming, graphic design just to list a few and one can select the amount of difficulty one is able to handle from the api',
        terms_of_service = 'https://google.com/policies/terms',
        contact = openapi.Contact(email='githinjianthony720@gmail.com'),
        license = openapi.license(name='MIT License'),
    )

)

urlpatterns = [
    path('admin/', admin.site.urls),
]
