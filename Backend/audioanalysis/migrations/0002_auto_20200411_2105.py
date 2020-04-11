# Generated by Django 3.0.5 on 2020-04-11 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioanalysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='audio',
        ),
        migrations.AddField(
            model_name='audio',
            name='s3_url',
            field=models.URLField(default='RANDOM TEXT', max_length=500),
        ),
    ]
