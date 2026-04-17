from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import json

from uploads.views import upload_image

def home(request):
    return JsonResponse({"message": "API is working"})

@csrf_exempt
def test_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({"received": data})
    return JsonResponse({"error": "POST only"}, status=400)

urlpatterns = [
    path('', home),
    path('test/', test_post),
    path('admin/', admin.site.urls),
    path('upload/', upload_image),
]