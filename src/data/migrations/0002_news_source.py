# Generated by Django 5.1 on 2024-08-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="source",
            field=models.URLField(blank=True, null=True),
        ),
    ]
