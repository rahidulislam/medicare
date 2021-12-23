from django.db import models

# Create your models here.
class Appointment(models.Model):
    """Patient can appointment"""
    name = models.CharField(("Name"), max_length=100)
    phone = models.CharField(("Phone Number"), max_length=50)
    email = models.EmailField(("Email"), max_length=254)
    appointment_date = models.DateField(("Appointment Date"))
    note = models.TextField(("Note"))

    def __str__(self):
        return self.name