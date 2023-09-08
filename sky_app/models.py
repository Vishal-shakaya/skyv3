from django.db import models
from django.contrib.auth.models import User
# Create your models here.


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
