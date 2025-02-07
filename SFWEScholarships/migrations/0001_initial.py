# Generated by Django 5.0.1 on 2024-03-20 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ScholarshipDonor', '0001_initial'),
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stauts', models.CharField(choices=[('Submitted', 'Submitted'), ('In Reivew', 'In Review'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Submitted', max_length=20)),
                ('essay', models.TextField()),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScholarshipDonor.scholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.student')),
            ],
        ),
    ]
