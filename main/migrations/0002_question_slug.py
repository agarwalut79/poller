# Generated by Django 3.0.2 on 2020-07-12 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='question'),
            preserve_default=False,
        ),
    ]
