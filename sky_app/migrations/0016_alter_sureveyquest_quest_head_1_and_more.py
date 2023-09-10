# Generated by Django 4.2.4 on 2023-09-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sky_app', '0015_sureveyquest_no_10_sureveyquest_no_11_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sureveyquest',
            name='quest_head_1',
            field=models.CharField(blank=True, default='Does business have missed-call text-back in place?', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sureveyquest',
            name='quest_head_2',
            field=models.CharField(blank=True, default='Does website have a text-enabled phone number?', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sureveyquest',
            name='quest_head_3',
            field=models.CharField(blank=True, default='Does website have an SMS chat widget?', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sureveyquest',
            name='quest_head_4',
            field=models.CharField(blank=True, default='Is Google Business Chat enabled?', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sureveyquest',
            name='quest_head_5',
            field=models.CharField(blank=True, default='Are popular listings in place and in order?', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sureveyquest',
            name='quest_head_6',
            field=models.CharField(blank=True, default='Does business have a consolidated conversation stream? Is it mobile-friendly?', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sureveyquest',
            name='quest_head_7',
            field=models.CharField(blank=True, default='Is business leveraging Text Snippets or auto-replies for FAQs?', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sureveyquest',
            name='quest_head_8',
            field=models.CharField(blank=True, default='Is the business set up to send personalized video messages to leads?', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sureveyquest',
            name='quest_head_9',
            field=models.CharField(blank=True, default='Does the business have Text-2-Pay?', max_length=255, null=True),
        ),
    ]