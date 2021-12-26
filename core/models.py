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

class Faq(models.Model):
    title = models.CharField(("FAQ Title"), max_length=150)
    description = models.TextField(("FAQ Description"))

    def __str__(self):
        return self.title

class ClientSay(models.Model):
    name = models.CharField(("Client Name"), max_length=50)
    designation = models.CharField(("Client Designation"), max_length=50)
    description = models.TextField(("Clent Feedback"))
    image = models.ImageField(("Client Image"), upload_to="client", blank=True)

    def __str__(self):
        return self.name

    def image_url(self):
        """Testimonial image url"""
        try:
            url = self.image.url
        except:
            url = ''
        return url
