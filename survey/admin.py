from django.contrib import admin

# Register your models here.
from .models import Grade, Questions, Answers

admin.site.register(Grade)
admin.site.register(Questions)
admin.site.register(Answers)