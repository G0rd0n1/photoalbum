# Generated by Django 4.1.2 on 2022-10-24 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pAlbum", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Images",
            new_name="Image",
        ),
    ]