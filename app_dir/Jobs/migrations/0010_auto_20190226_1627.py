# Generated by Django 2.1.5 on 2019-02-26 10:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Jobs', '0009_appliedjob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedjob',
            name='applicant',
        ),
        migrations.AddField(
            model_name='appliedjob',
            name='applicant',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
