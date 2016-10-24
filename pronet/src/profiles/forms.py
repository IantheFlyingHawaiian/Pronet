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
            Field('skills'),
            Field('work_years'),
            Field('degree'),
            Field('resume'),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.Profile
        fields = ['picture', 'bio', 'skills', 'work_years', 'degree', 'resume',]


class WorkExperienceForm(forms.ModelForm):
    """
    Form for entering individual work experiences.
    """

    def __init__(self, *args, **kwargs):
        super(WorkExperienceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            #Field('start_date'),
            #Field('end_date'),
            #Field('current'),
            #Field('location'),
            #Field('details'),
            #Field('company'),
            #Field('title'),
            MultiField(
                'Work Experience',
                'start_date',
                'end_date',
                'current',
                'location',
                'details',
                'company',
                'title',
            ),
        )

    class Meta:
        model = models.WorkExperience
        fields = ['start_date', 'end_date', 'current', 'location', 'details', 'company', 'title',]
