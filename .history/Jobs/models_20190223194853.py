from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class JobPost(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    job_type = (
        ('part-time', 'Part Time'),
        ('full-time', 'Full Time'),
        ('internship', 'Internship'),
    )
    job_type = models.CharField(choices=job_type, max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_type = (
        ('featured', 'FEATURED'),
        ('standard', 'STANDARD'),

    )
    post_type = models.CharField(choices=post_type, max_length=200)
    apply_url = models.URLField(name=None, null=True, blank=True)
    validity = models.DateTimeField(auto_now_add=True)

    company_name = models.CharField(max_length=100, null=True, blank=True)
    company_description = models.TextField(null=True, blank=True)
    company_website = models.URLField(name=None, null=True, blank=True)
    company_logo = models.ImageField(upload_to="solution", help_text="top left image", null=True, blank=True)
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