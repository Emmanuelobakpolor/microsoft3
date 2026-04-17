from django.http import JsonResponse
from .models import UploadedImage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        image = request.FILES.get("image")

        if not image:
            return JsonResponse({"error": "No image uploaded"}, status=400)

        obj = UploadedImage.objects.create(image=image)

        return JsonResponse({
            "message": "Uploaded successfully",
            "image_url": obj.image.url
        })

    return JsonResponse({"error": "POST only"}, status=400)