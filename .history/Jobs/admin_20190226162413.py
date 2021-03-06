from django.contrib import admin
from .models import JobPost, Category, Profile, AppliedJob

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Category)
admin.site.register(Profile)


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'created_at', 'updated_at']

admin.site.register(AppliedJob, UserAdmin)