# Generated by Django 5.1 on 2024-08-09 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0002_news_source"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"verbose_name_plural": "News"},
        ),
    ]
