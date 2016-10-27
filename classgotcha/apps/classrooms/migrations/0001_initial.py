# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.CharField(max_length=100)),
                ('class_number', models.IntegerField()),
                ('class_code', models.IntegerField()),
                ('syllabus', models.URLField(null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('major', models.ForeignKey(to='accounts.Major')),
                ('professor', models.ManyToManyField(related_name='teaches', to=settings.AUTH_USER_MODEL, blank=True)),
                ('students', models.ManyToManyField(related_name='classrooms', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
    ]
