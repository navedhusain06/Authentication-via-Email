# Generated by Django 5.1 on 2024-09-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogReg_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email_token',
            new_name='auth_token',
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
