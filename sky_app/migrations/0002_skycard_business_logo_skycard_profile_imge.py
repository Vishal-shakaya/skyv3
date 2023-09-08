# Generated by Django 4.2.4 on 2023-09-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sky_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skycard',
            name='business_logo',
            field=models.FileField(blank=True, null=True, upload_to='logos'),
        ),
        migrations.AddField(
            model_name='skycard',
            name='profile_imge',
            field=models.FileField(blank=True, null=True, upload_to='profiles'),
        ),
    ]
