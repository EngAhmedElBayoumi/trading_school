# Generated by Django 4.2.4 on 2024-09-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("landing_page", "0010_video_message"),
    ]

    operations = [
        migrations.AddField(
            model_name="userrequested",
            name="conected",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="userrequested",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="userrequested",
            name="mynotes",
            field=models.TextField(blank=True, null=True),
        ),
    ]
