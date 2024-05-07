# Generated by Django 5.0.1 on 2024-05-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SFWEScholarships', '0006_remove_application_resume_alter_application_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='resume',
            field=models.FileField(default=1, upload_to='resumes/'),
            preserve_default=False,
        ),
    ]
