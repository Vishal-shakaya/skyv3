# Generated by Django 4.2.4 on 2023-09-08 12:56

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sky_app', '0009_blog_creaded_by_blog_timestamp_testimonial_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]
