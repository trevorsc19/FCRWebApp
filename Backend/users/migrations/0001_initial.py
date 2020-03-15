# Generated by Django 2.2.4 on 2020-03-15 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists'}, help_text='Required. 150 Characters or fewer', max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site', verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Whether the user is a superuser', verbose_name='Superuser status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
    ]
