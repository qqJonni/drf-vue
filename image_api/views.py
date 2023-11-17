from django.shortcuts import render
from .serializers import ImageSerializer
from rest_framework.viewsets import ModelViewSet
from image_api.models import Image


class ImageModelViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


def images_page(request):
    return render(request, 'main_app.html')

