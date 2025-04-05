from django.contrib import admin
from .models import StudentInfo
from django.contrib import admin
from .models import Assignments, Wellness  # Ensure these exist in models.py





admin.site.register(StudentInfo)
admin.site.register(Assignments)
admin.site.register(Wellness)

