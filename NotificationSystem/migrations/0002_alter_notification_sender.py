# Generated by Django 5.0.2 on 2024-05-07 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NotificationSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.CharField(max_length=100),
        ),
    ]
