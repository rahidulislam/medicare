from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    banner_image = models.ImageField(upload_to='banner/', blank=True)

    def __str__(self):
        return self.title

    def image_url(self):
        """banner image url"""
        try:
            url = self.banner_image.url
        except:
            url = ''
        return url


