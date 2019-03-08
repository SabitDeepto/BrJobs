# Generated by Django 2.1.5 on 2019-03-02 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Jobs', '0013_auto_20190302_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedjob',
            name='total_applied',
        ),
        migrations.RemoveField(
            model_name='appliedjob',
            name='applicant',
        ),
        migrations.AddField(
            model_name='appliedjob',
            name='applicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]