# Generated by Django 4.2.4 on 2023-10-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sky_app', '0025_alter_partnerus_category_alter_partnerus_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]