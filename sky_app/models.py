from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django_quill.fields import QuillField
from datetime import datetime


class Blog(models.Model):
    content = QuillField(null=True, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    thumbnail = models.FileField(upload_to='thumbnail', null=True, blank=True)
    heading = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(
        auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.pk} {self.heading} {self.timestamp}'


class MetaTags(models.Model):
    metatag = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.metatag} {self.pk}'


class Testimonial(models.Model):
    thumbnail = models.FileField(
        upload_to='testimonial', null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.pk}'


class SkyCard(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.FileField(
        upload_to='profiles', null=True, blank=True)
    business_logo = models.FileField(upload_to='logos', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    whats_app_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    insta = models.CharField(max_length=500, null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    youtube = models.CharField(max_length=500, null=True, blank=True)

    business_name = models.CharField(max_length=255, null=True, blank=True)
    business_heading = models.CharField(max_length=255, null=True, blank=True)
    gst_number = models.CharField(max_length=255, null=True, blank=True)
    stablish_year = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=500, null=True, blank=True)
    tagline = models.CharField(max_length=255, null=True, blank=True)
    tag = models.CharField(max_length=255, null=True, blank=True)
    business_description = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.number} {self.business_name}'


class SureveyQuest(models.Model):
    email = models.EmailField(blank=True, null=True)
    total_score = models.IntegerField(blank=True, null=True)

    solution = models.TextField(null=True, blank=True)

    quest_head_1 = models.CharField(
        default='Does business have missed-call text-back in place?',
        max_length=255, null=True, blank=True)
    yes_1 = models.BooleanField(default=False,)
    no_1 = models.BooleanField(default=False)

    quest_head_2 = models.CharField(
        default='Does website have a text-enabled phone number?',
        max_length=255, null=True, blank=True)
    yes_2 = models.BooleanField(default=False)
    no_2 = models.BooleanField(default=False)

    quest_head_3 = models.CharField(
        default='Does website have an SMS chat widget?',
        max_length=255, null=True, blank=True)
    yes_3 = models.BooleanField(default=False)
    no_3 = models.BooleanField(default=False)

    quest_head_4 = models.CharField(
        default='Is Google Business Chat enabled?',
        max_length=255, null=True, blank=True)
    yes_4 = models.BooleanField(default=False)
    no_4 = models.BooleanField(default=False)

    quest_head_5 = models.CharField(
        default='Are popular listings in place and in order?',
        max_length=255, null=True, blank=True)
    yes_5 = models.BooleanField(default=False)
    no_5 = models.BooleanField(default=False)

    quest_head_6 = models.CharField(
        default='Does business have a consolidated conversation stream? Is it mobile-friendly?',
        max_length=255, null=True, blank=True)
    yes_6 = models.BooleanField(default=False)
    no_6 = models.BooleanField(default=False)

    quest_head_7 = models.CharField(
        default='Is business leveraging Text Snippets or auto-replies for FAQs?',
        max_length=255, null=True, blank=True)
    yes_7 = models.BooleanField(default=False,)
    no_7 = models.BooleanField(default=False)

    quest_head_8 = models.CharField(
        default='Is the business set up to send personalized video messages to leads?',
        max_length=255, null=True, blank=True)
    yes_8 = models.BooleanField(default=False,)
    no_8 = models.BooleanField(default=False)

    quest_head_9 = models.CharField(
        default='Does the business have Tap-2-Pay?',
        max_length=255, null=True, blank=True)
    yes_9 = models.BooleanField(default=False,)
    no_9 = models.BooleanField(default=False)

    quest_head_10 = models.CharField(
        default='Tap to pay turns smartphones into credit card readers, enabling payment anywhere',
        max_length=255, null=True, blank=True)
    yes_10 = models.BooleanField(default=False,)
    no_10 = models.BooleanField(default=False)

    quest_head_11 = models.CharField(
        default="Does business have an acceptable rating?",
        max_length=255, null=True, blank=True)
    yes_11 = models.BooleanField(default=False,)
    no_11 = models.BooleanField(default=False)

    quest_head_12 = models.CharField(
        default="Are reviews being generated frequently and consistently?",
        max_length=255, null=True, blank=True)
    yes_12 = models.BooleanField(default=False,)
    no_12 = models.BooleanField(default=False)

    quest_head_13 = models.CharField(
        default='Are reviews being replied to?',
        max_length=255, null=True, blank=True)
    yes_13 = models.BooleanField(default=False,)
    no_13 = models.BooleanField(default=False)

    quest_head_14 = models.CharField(
        default='Does business have a database of emails and phone numbers?',
        max_length=255, null=True, blank=True)
    yes_14 = models.BooleanField(default=False,)
    no_14 = models.BooleanField(default=False)

    quest_head_15 = models.CharField(
        default='Does business have a way to send bulk email/sms?',
        max_length=255, null=True, blank=True)
    yes_15 = models.BooleanField(default=False,)
    no_15 = models.BooleanField(default=False)

    quest_head_16 = models.CharField(
        default='Does business have a Newsletter Builder?',
        max_length=255, null=True, blank=True)
    yes_16 = models.BooleanField(default=False,)
    no_16 = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quest_head_1} {self.pk}'


class PartnerUs(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField()

    def __str__(self):
        return self.name
