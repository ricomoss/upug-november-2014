# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FibHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('fib_index', models.PositiveIntegerField()),
                ('fib_num', models.TextField(max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
