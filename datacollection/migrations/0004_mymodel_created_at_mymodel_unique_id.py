# Generated by Django 4.1.13 on 2024-04-22 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacollection', '0003_merge_20240422_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='created_at',
            field=models.DateTimeField(default='2024-04-22'),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='unique_id',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
