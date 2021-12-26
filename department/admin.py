from django.contrib import admin
from department.models import Department, Doctor, Service
# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Service)
