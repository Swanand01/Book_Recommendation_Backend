# Generated by Django 4.1.4 on 2023-01-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]