# Generated by Django 3.0.5 on 2020-04-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioanalysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='audio_file',
            field=models.FileField(null=True, upload_to='audio/'),
        ),
    ]
