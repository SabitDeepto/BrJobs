from django.db import models
from django.utils.text import slugify

# Create your models here.


class JobPost(models.Model):
    last_3_digit = models.IntegerField(null=True)
    transaction_id = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    gender_choice = (
        ('done', 'DONE'),
        ('pending', 'PENDING'),
    )
    status = models.CharField(choices=gender_choice, max_length=200)