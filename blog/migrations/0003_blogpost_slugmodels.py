# Generated by Django 4.2 on 2023-05-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_title_blogpost_titlemodels_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slugModels',
            field=models.SlugField(default='hello world'),
        ),
    ]
