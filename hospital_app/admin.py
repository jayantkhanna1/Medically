from django.contrib import admin
from .models import patient,staff,Doctor
# Register your models here.
admin.site.register(patient)
admin.site.register(staff)
admin.site.register(Doctor)