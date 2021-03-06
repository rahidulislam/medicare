from django.shortcuts import redirect, render
from django.views.generic import View
from core.models import Banner, ClientSay, Faq
from core.forms import AppointmentForm
from django.contrib import messages
from department.models import Department, Doctor, Service
# Create your views here.

class HomeView(View):
    template_name = 'core/index.html'
    
    def get(self, request):
        banners = Banner.objects.all().order_by('-id')[:5]
        departments = Department.objects.all()
        doctors = Doctor.objects.all()
        services = Service.objects.all()
        faqs = Faq.objects.all()
        testimonials = ClientSay.objects.all()
        appointment_form = AppointmentForm
        context = {
            'banners': banners,
            'appointment_form': appointment_form,
            'departments': departments,
            'doctors': doctors,
            'services': services,
            'faqs': faqs,
            'testimonials': testimonials
        }
        return render(request, self.template_name, context)

    def post(self, request):
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save()
            messages.success(request, "Your Appointment is submited Successfully")
            return redirect('core:home')
        return render(request, self.template_name, {'appointment_form': appointment_form})