# Generated by Django 5.0.1 on 2024-05-06 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicantReviewer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicantreviewer',
            old_name='applicantReviewer_info',
            new_name='applicantReviewer_info_id',
        ),
    ]
