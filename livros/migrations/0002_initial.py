# Generated by Django 4.1.7 on 2023-03-06 15:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("livros", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="users",
            field=models.ManyToManyField(
                related_name="following", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]