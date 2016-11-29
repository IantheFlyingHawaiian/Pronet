from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, MultiField
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
            )

    class Meta:
        model = User
        fields = ['name']


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('picture'),
            Field('bio'),
            Field('work_years'),
            Field('degree'),
            Field('resume'),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.Profile
        fields = ['picture', 'bio', 'work_years', 'degree', 'resume',]


class EditWorkExperienceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditWorkExperienceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('start_date'),
            Field('end_date'),
            Field('current'),
            Field('location'),
            Field('details'),
            Field('company'),
            Field('title'),
            Submit('update', 'Update', css_class="btn-success"),
        )

    class Meta:
        model = models.WorkExperience
        fields = ['start_date', 'end_date', 'current', 'location', 'details', 'company', 'title',]


class AddWorkExperienceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddWorkExperienceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('start_date'),
            Field('end_date'),
            Field('current'),
            Field('location'),
            Field('details'),
            Field('company'),
            Field('title'),
            Submit('add', 'Add', css_class="btn-success"),
        )

    class Meta:
        model = models.WorkExperience
        fields = ['start_date', 'end_date', 'current', 'location', 'details', 'company', 'title',]


class EditSkillExperienceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditSkillExperienceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('skill_name'),
            Field('skill_years'),
            Field('end_photo1'),
            Field('end_photo2'),
            Field('end_photo3'),
            Field('end_photo4'),
            Field('end_count'),
            Submit('update', 'Update', css_class="btn-success"),
        )

    class Meta:
        model = models.SkillExperience
        fields = ['skill_name', 'skill_years', 'end_photo1', 'end_photo2', 'end_photo3', 'end_photo4', 'end_count', ]


class AddSkillExperienceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddSkillExperienceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('skill_name'),
            Field('skill_years'),
            Field('end_photo1'),
            Field('end_photo2'),
            Field('end_photo3'),
            Field('end_photo4'),
            Field('end_count'),
            Submit('add', 'Add', css_class="btn-success"),
        )

    class Meta:
        model = models.SkillExperience
        fields = ['skill_name', 'skill_years', 'end_photo1', 'end_photo2', 'end_photo3', 'end_photo4', 'end_count',]
