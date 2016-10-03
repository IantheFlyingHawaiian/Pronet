from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)
    skills = models.CharField("Skills", max_length=200, blank=True, null=True)
    work_years = models.DecimalField("Years Worked", max_digits=4, decimal_places=2, blank=True, null=True)
    degree = models.CharField("Degree", max_length=200, blank=True, null=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)

class University(models.Model):
    country = models.CharField("Country Abbreviation", max_length=2, blank=True, null=True)
    name = models.CharField("Name", max_length=200, blank=True, null=True)
    website = models.CharField("Website", max_length=200, blank=True, null=True)

    def __str__(self):
        return "{0}, {1} ({2})".format(self.country, self.name, self.website)


    class Meta:
        ordering = ['country', 'name']
