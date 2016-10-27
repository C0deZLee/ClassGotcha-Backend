# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('image', models.URLField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(related_name='comments', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('moment', models.ForeignKey(related_name='comments', blank=True, to='posts.Moment', null=True)),
                ('post', models.ForeignKey(related_name='comments', blank=True, to='posts.Post', null=True)),
            ],
        ),
    ]
