# Generated by Django 4.1.2 on 2023-09-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sky_app', '0005_alter_skycard_address_alter_skycard_business_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skycard',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skycard',
            name='business_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
