# Generated by Django 5.2 on 2025-04-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyses',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/analyse_images'),
        ),
    ]
