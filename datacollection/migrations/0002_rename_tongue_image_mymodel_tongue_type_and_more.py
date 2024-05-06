# Generated by Django 4.1.13 on 2024-04-06 04:51

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("datacollection", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mymodel",
            old_name="tongue_image",
            new_name="tongue_type",
        ),
        migrations.RemoveField(
            model_name="mymodel",
            name="pulse_csv_path",
        ),
        migrations.AddField(
            model_name="mymodel",
            name="pulse_type",
            field=models.CharField(default="default_value", max_length=100),
        ),
    ]
