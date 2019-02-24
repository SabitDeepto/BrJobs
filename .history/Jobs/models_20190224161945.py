from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe
# Create your models here.

## User Profile


class User(AbstractUser):
    is_compnay = models.BooleanField(default=False)
    is_freelancer = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    # def __str__(self):
    #     return self.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


## job purpose
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class JobPost(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    job_type = (
        ('part-time', 'Part Time'),
        ('full-time', 'Full Time'),
        ('internship', 'Internship'),
    )
    jobtype = models.CharField(choices=job_type, max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_type = (
        ('featured', 'FEATURED'),
        ('standard', 'STANDARD'),

    )
    post_type = models.CharField(choices=post_type, max_length=200)
    apply_url = models.URLField(name=None, null=True, blank=True)
    # validity = models.DateTimeField(auto_now_add=True)

    company_name = models.CharField(max_length=100, null=True, blank=True)
    company_description = models.TextField(null=True, blank=True)
    company_website = models.URLField(name=None, null=True, blank=True)
    company_logo = models.ImageField(upload_to="logo", help_text="top left image", null=True, blank=True)
    twitter_link = models.URLField(name=None, null=True, blank=True)

    slug = models.SlugField(null=True, blank=True, help_text="Slug will be generated automatically from the title_2 of the post")

    class Meta:
        verbose_name_plural = 'Job Post'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(JobPost, self).save(*args, **kwargs)