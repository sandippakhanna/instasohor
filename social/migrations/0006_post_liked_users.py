# Generated by Django 3.1.2 on 2021-01-05 14:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
