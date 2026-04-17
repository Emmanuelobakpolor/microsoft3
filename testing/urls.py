"""
URL configuration for testing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import JsonResponse
from django.urls import path
import json

def home(request):
    return JsonResponse({"message": "API is working"})

def test_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({
            "received": data
        })
    return JsonResponse({"error": "POST only"}, status=400)

urlpatterns = [
    path('', home),
    path('test/', test_post),
    path('admin/', admin.site.urls),
]