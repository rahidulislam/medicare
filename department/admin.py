from django.contrib import admin
from core.models import Faq
from department.models import Department, Doctor, Service
# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Faq)