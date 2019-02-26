from django.contrib import admin
from . models import  User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'created_at']
    # fieldsets = (
    #     ('Service Title for Index Page', {
    #         'fields': ('title_1', 'subtitle_1')
    #     }),
    #     ('Service Main Text', {
    #         'fields': ('title_2', 'subtitle_2', 'button', 'heading_1', 'heading_2', 'description',  'l_image', 'r_image', 'm_image')
    #     }),
    #     ('Service Extra Field 1 (Not Mandetory !You can skip this Section )', {
    #         'fields': ('extra_title_1', 'extra_description_1', 'extra_image_1', 'additional_resource_text_1', 'additional_resource_metatext_1', 'additional_resource_url_a', 'additional_resource_url_b',)
    #     }),
    #     ('Service Extra Field 2 (Not Mandetory !You can skip this Section )', {
    #         'fields': ('extra_title_2', 'extra_description_2', 'extra_image_2', 'additional_resource_text_2', 'additional_resource_metatext_2', 'additional_resource_url_c', 'additional_resource_url_d',)
    #     }),

    # )

admin.site.register(User, UserAdmin)