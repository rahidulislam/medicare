from django import forms
from appointment.models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone Number', 'type': 'tel'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}),
            'appointment_date' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Phone Number'})
        }
