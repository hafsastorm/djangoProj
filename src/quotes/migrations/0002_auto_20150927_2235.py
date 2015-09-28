# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('author', models.CharField(max_length=50)),
                ('book', models.CharField(max_length=50, null=True, blank=True)),
                ('passage', models.CharField(max_length=500, serialize=False, primary_key=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Quotes',
        ),
    ]
