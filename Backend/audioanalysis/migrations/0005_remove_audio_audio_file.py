# Generated by Django 3.0.5 on 2020-05-03 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audioanalysis', '0004_auto_20200503_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='audio_file',
        ),
    ]
