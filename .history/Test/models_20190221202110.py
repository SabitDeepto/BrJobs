from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_freelancer = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    institute = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.username


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
