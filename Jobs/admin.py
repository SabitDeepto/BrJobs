from django.contrib import admin
from .models import JobPost, Category

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Category)
