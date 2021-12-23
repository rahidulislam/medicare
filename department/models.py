from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(("Department"), max_length=100)
    short_description = models.TextField(("Short Description"))
    image = models.ImageField(upload_to='department/', blank=True)

    def __str__(self):
        return self.title

    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Doctor(models.Model):
    department = models.ForeignKey(Department, verbose_name=("Doctor Department"), on_delete=models.CASCADE, related_name='doctor_department')
    name = models.CharField(("Doctor Name"), max_length=100)
    designation = models.CharField(("Doctor Designation"), max_length=100)
    image = models.ImageField(upload_to='doctor/', blank=True)

    def __str__(self):
        return self.name

    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Service(models.Model):
    department = models.ForeignKey(Department, verbose_name=("Department"), on_delete=models.CASCADE, related_name='department_service')
    name = models.CharField(max_length=100)
    short_description = models.TextField(("Short Description"), blank=True)
    description = models.TextField(("Description"), blank=True)
    image = models.ImageField(("Service Image"), upload_to='service/', blank=True)

    def __str__(self):
        return self.name

    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url