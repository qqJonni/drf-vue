from django.shortcuts import render
from .serializers import ImageSerializer
from rest_framework.viewsets import ModelViewSet
from image_api.models import Image
from rest_framework.response import Response
from rest_framework import status


class ImageModelViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


def images_page(request):
    return render(request, 'main_app.html')

