from django.db import models
from django.utils.text import slugify

# Create your models here.


class JobPost(models.Model):
    title_1 = models.CharField(max_length=100, null=True, blank=True)
    subtitle_1 = models.CharField(max_length=150, null=True, blank=True)
    title_2 = models.CharField(max_length=100, null=True, blank=True)
    subtitle_2 = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, help_text="Slug will be generated automatically from the title_2 of the post")
    button = models.CharField(max_length=30, null=True, blank=True)
    heading_1 = models.CharField(max_length=100, null=True, blank=True)
    heading_2 = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    l_image = models.ImageField(upload_to="solution", help_text="top left image", null=True, blank=True)
    r_image = models.ImageField(upload_to="solution", help_text="top right image", null=True, blank=True)
    m_image = models.ImageField(upload_to="solution", help_text="your main image", null=True, blank=True)
    last_3_digit = models.IntegerField(null=True)
    transaction_id = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    gender_choice = (
        ('done', 'DONE'),
        ('pending', 'PENDING'),
    )
    status = models.CharField(choices=gender_choice, max_length=200)