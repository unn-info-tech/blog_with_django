# Generated by Django 4.2 on 2023-05-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_slugmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slugModels',
            field=models.SlugField(unique=True),
        ),
    ]
