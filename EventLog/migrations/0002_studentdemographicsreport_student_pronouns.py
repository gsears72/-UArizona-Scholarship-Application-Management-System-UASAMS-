# Generated by Django 5.0.1 on 2024-05-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventLog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdemographicsreport',
            name='Student_Pronouns',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
