"""Tarea1 URL Configuration

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
from Tarea1.views import index, contact, episode, character, location, episodes, locations, characters
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contact/', contact),
    path('episodes/', episodes),
    path('locations/', locations),
    path('characters/', characters),
    path('episode/<int:number>', episode),
    path('character/<int:number>', character),
    path('location/<int:number>', location)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
