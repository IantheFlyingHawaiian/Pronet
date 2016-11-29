from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
import os


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)
    work_years = models.DecimalField("Years Worked", max_digits=4, decimal_places=0, blank=True, null=True)
    degree = models.CharField("Degree", max_length=200, blank=True, null=True)
    resume = models.FileField("Resume",
                              upload_to='resumes/%Y-%m-%d/',
                              null = True,
                              blank = True)
    premium_flag = models.BooleanField("Premium User", default=False)
    connections = models.ManyToManyField('self', through='Connection', symmetrical=False, related_name='connections_set')

    def resume_name(self):
        return os.path.basename(self.resume.name)


    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{0}'s profile".format(self.user)


class University(models.Model):
    country = models.CharField("Country Abbreviation", max_length=2, blank=True, null=True)
    name = models.CharField("Name", max_length=200, blank=True, null=True)
    website = models.CharField("Website", max_length=200, blank=True, null=True)

    def __str__(self):
        return "{0}, {1}, {2}".format(self.country, self.name, self.website)

    class Meta:
        ordering = ['country', 'name']


class SkillExperience(models.Model):
    profile = models.ForeignKey(Profile)
    skill_name = models.CharField('Skill', max_length=200)
    skill_years = models.DecimalField('Years Known', max_digits=4, decimal_places=0, blank=True, null=True)
    end_photo1 = models.ImageField('Endorser 1', null=True, blank=True)
    end_photo2 = models.ImageField('Endorser 2', null=True, blank=True)
    end_photo3 = models.ImageField('Endorser 3', null=True, blank=True)
    end_photo4 = models.ImageField('Endorser 4', null=True, blank=True)
    end_count = models.DecimalField('Endorser Count', max_digits=4, decimal_places=0, blank=True, null=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)

    def __str__(self):
        return "Skill for {0}, with skill {1} for years {2}".format(self.profile, self.skill_name, self.skill_years)

    class Meta:
        ordering = ['-skill_name', '-skill_years', '-end_count']


class WorkExperience(models.Model):
    profile = models.ForeignKey(Profile)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date', blank=True, null=True)
    current = models.BooleanField('Current Position', default=False)
    location = models.CharField('Location', max_length=200)
    details = models.TextField('Details', blank=True)
    company = models.CharField('Company', max_length=200)
    title = models.CharField('Position Titile', max_length=200)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)

    def __str__(self):
        return "Work for {0}, started {1}, at {2}".format(self.profile, self.start_date, self.company)


    class Meta:
        ordering = ['-current', '-start_date', '-end_date']


class Connection(models.Model):
    # Profile that initiates the connection request is always profile1
    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile1')
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile2')
    time = models.DateTimeField('Connection Timestamp', auto_now=True)
    pending = models.BooleanField('Connection Pending', default=True)

    def __str__(self):
        return "Connection between {0} and {1}".format(self.profile1, self.profile2)