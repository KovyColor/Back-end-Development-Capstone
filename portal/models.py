from django.db import models


class FavoritePicture(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
