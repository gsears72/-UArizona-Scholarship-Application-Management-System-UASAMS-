# Generated by Django 5.0.2 on 2024-05-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0011_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='yiwrchzhfm@test.com', max_length=60, unique=True, verbose_name='email'),
        ),
    ]
