from django.db import models


class Image(models.Model):
    description = models.TextField()
    image_data = models.TextField()

