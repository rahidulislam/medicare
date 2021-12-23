from django.shortcuts import render
from django.views.generic import View
from core.models import Banner
# Create your views here.

class HomeView(View):
    template_name = 'core/index.html'
    
    def get(self, request):
        banners = Banner.objects.all().order_by('-id')[:5]
        doctors = Banner.objects.all()
        context = {
            'banners': banners,
            'doctors': doctors
        }
        return render(request, self.template_name, context)