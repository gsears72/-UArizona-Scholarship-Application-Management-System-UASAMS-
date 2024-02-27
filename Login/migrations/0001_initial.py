# Generated by Django 5.0.2 on 2024-02-17 06:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=128)),
                ('Security_Question1', models.CharField(max_length=130)),
                ('Security_Question1_answer', models.CharField(max_length=30)),
                ('Security_Question2', models.CharField(max_length=130)),
                ('Security_Question2_answer', models.CharField(max_length=30)),
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Phone_number', models.CharField(max_length=30)),
                ('Net_ID', models.CharField(blank=True, max_length=30)),
                ('role', models.CharField(choices=[('Student', 'Student'), ('Scholarship Administrator', 'Scholarship Administrator'), ('Applicant Reviewer', 'Applicant Reviewer'), ('Scholarship Donor', 'Scholarship Donor'), ('Authorized ENGR Staff', 'Authorized ENGR Staff'), ('ENGR IT Support Staff', 'ENGR IT Support Staff')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicantReviewer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Login.user',),
        ),
        migrations.CreateModel(
            name='AuthorizedENGRStaffent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Login.user',),
        ),
        migrations.CreateModel(
            name='ENGRITSupportStaff',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Login.user',),
        ),
        migrations.CreateModel(
            name='ScholarshipAdministrator',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Login.user',),
        ),
        migrations.CreateModel(
            name='ScholarshipDonor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Login.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Login.user',),
        ),
    ]
