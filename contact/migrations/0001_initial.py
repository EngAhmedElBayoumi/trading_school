# Generated by Django 4.2.4 on 2024-09-06 22:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("create_by", models.CharField(max_length=100)),
                ("ended_at", models.DateTimeField(blank=True, null=True)),
                ("subject", models.CharField(max_length=100)),
                ("message", models.TextField()),
            ],
        ),
    ]
