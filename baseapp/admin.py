from django.contrib import admin
from .models import Student,MagStaff,Holiday, Reviews, Complaints
# Register your models here.
admin.site.register(Student)
admin.site.register(MagStaff)
admin.site.register(Holiday)
admin.site.register(Complaints)
admin.site.register(Reviews)