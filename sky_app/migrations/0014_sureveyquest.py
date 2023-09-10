# Generated by Django 4.2.4 on 2023-09-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sky_app', '0013_rename_creaded_by_blog_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='SureveyQuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_head_1', models.CharField(blank=True, max_length=255, null=True)),
                ('yes_1', models.BooleanField(default=False)),
                ('no_1', models.BooleanField(default=False)),
                ('quest_head_2', models.CharField(blank=True, max_length=255, null=True)),
                ('yes_2', models.BooleanField(default=False)),
                ('no_2', models.BooleanField(default=False)),
                ('quest_head_3', models.CharField(blank=True, max_length=255, null=True)),
                ('yes_3', models.BooleanField(default=False)),
                ('no_3', models.BooleanField(default=False)),
                ('quest_head_4', models.CharField(blank=True, max_length=255, null=True)),
                ('yes_4', models.BooleanField(default=False)),
                ('no_4', models.BooleanField(default=False)),
                ('quest_head_5', models.CharField(blank=True, max_length=255, null=True)),
                ('yes_5', models.BooleanField(default=False)),
                ('no_5', models.BooleanField(default=False)),
                ('quest_head_6', models.CharField(blank=True, max_length=255, null=True)),
                ('yes_6', models.BooleanField(default=False)),
                ('no_6', models.BooleanField(default=False)),
            ],
        ),
    ]
