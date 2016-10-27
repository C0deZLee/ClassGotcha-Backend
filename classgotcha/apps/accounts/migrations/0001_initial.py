# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('username', models.CharField(unique=True, max_length=40)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=True)),
                ('is_professor', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=40, blank=True)),
                ('mid_name', models.CharField(max_length=40, blank=True)),
                ('last_name', models.CharField(max_length=40, blank=True)),
                ('gender', models.CharField(max_length=40, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('school_year', models.CharField(max_length=40, blank=True)),
                ('avatar', models.URLField(blank=True)),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('major_short', models.CharField(max_length=10)),
                ('major_full', models.CharField(max_length=100)),
                ('major_college', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='major',
            field=models.ForeignKey(blank=True, to='accounts.Major', null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]
