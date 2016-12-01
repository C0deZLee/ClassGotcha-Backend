# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_type', models.CharField(max_length=20)),
                ('classroom', models.ForeignKey(related_name='groups', blank=True, to='classrooms.Classroom', null=True)),
                ('creator', models.ForeignKey(related_name='created_groups', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='joined_groups', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
    ]
