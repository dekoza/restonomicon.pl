# Generated by Django 3.2.6 on 2021-08-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0002_belonging_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="friend",
            name="email",
            field=models.EmailField(default="", max_length=254),
        ),
    ]
