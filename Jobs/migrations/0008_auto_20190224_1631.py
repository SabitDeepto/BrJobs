# Generated by Django 2.1.5 on 2019-02-24 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0007_auto_20190224_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
