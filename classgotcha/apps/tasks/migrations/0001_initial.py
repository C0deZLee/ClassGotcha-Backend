# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=50)),
                ('task_des', models.CharField(max_length=500, blank=True)),
                ('start', models.DateTimeField(null=True, blank=True)),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('due_date', models.DateTimeField(null=True, blank=True)),
                ('type', models.CharField(max_length=50)),
                ('classroom', models.ForeignKey(related_name='tasks', blank=True, to='classrooms.Classroom', null=True)),
                ('group', models.ForeignKey(blank=True, to='groups.Group', null=True)),
                ('involved', models.ManyToManyField(related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
