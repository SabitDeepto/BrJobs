from django.contrib import admin
from .models import JobPost, Category, Profile

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Category)
admin.site.register(Profile)
