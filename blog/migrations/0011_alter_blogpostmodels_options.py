# Generated by Django 4.2 on 2023-07-10 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blogpostmodels_publushed_dateme_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpostmodels',
            options={'ordering': ['-publushed_dateME', '-timestampMe', '-updatedMe']},
        ),
    ]