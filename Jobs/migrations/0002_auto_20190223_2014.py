# Generated by Django 2.1.5 on 2019-02-23 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='job_type',
            new_name='jobtype',
        ),
    ]