# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_comment_related_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blogs.Post'),
        ),
    ]
