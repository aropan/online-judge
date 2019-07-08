# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-08 14:55
from __future__ import unicode_literals

from django.db import migrations, models


def updatecontestsubmissions(apps, schema_editor):
    ContestSubmissions = apps.get_model('judge', 'ContestSubmission')
    for row in ContestSubmissions.objects.all():
        submission = row.submission
        submission.is_locked = True
        submission.save()


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0086_rating_ceiling'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'permissions': (('abort_any_submission', 'Abort any submission'), ('rejudge_submission', 'Rejudge the submission'), ('rejudge_submission_lot', 'Rejudge a lot of submissions'), ('spam_submission', 'Submit without limit'), ('view_all_submission', 'View all submission'), ('resubmit_other', "Resubmit others' submission"), ('lock_submission', 'Change lock status of submission')), 'verbose_name': 'submission', 'verbose_name_plural': 'submissions'},
        ),
        migrations.AddField(
            model_name='submission',
            name='is_locked',
            field=models.BooleanField(default=False, verbose_name='lock submission'),
        ),
        migrations.RunPython(updatecontestsubmissions, reverse_code=migrations.RunPython.noop),
    ]
