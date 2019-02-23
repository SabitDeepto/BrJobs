from django.db import models
from django.utils.text import slugify

# Create your models here.


class JobPost(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    job_type = (
        ('part-time', 'Part Time'),
        ('full-time', 'Full Time'),
        ('internship', 'Internship'),
    )
    status = models.CharField(choices=gender_choice, max_length=200)
    title_2 = models.CharField(max_length=100, null=True, blank=True)
    subtitle_2 = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, help_text="Slug will be generated automatically from the title_2 of the post")
    button = models.CharField(max_length=30, null=True, blank=True)
    heading_1 = models.CharField(max_length=100, null=True, blank=True)
    heading_2 = models.CharField(max_length=100, null=True, blank=True)

    l_image = models.ImageField(upload_to="solution", help_text="top left image", null=True, blank=True)
    r_image = models.ImageField(upload_to="solution", help_text="top right image", null=True, blank=True)
    m_image = models.ImageField(upload_to="solution", help_text="your main image", null=True, blank=True)
    last_3_digit = models.IntegerField(null=True)
    transaction_id = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Job Post'

    def __str__(self):
        return self.title_1

    def save(self, *args, **kwargs):
        if not self.slug and self.title_2:
            self.slug = slugify(self.title_2)
        super(SolutionPost, self).save(*args, **kwargs)