# Generated by Django 4.2.4 on 2024-09-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("landing_page", "0002_benfitssection_description_ar_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="mainlandingpage",
            name="benfits_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="static/landing_page/image"
            ),
        ),
    ]
