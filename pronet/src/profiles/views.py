from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import formset_factory
from . import forms
from . import models


class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            profile = get_object_or_404(models.Profile, slug=slug)
            user = profile.user
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user
        return super(ShowProfile, self).get(request, *args, **kwargs)

class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "Profile details saved!")
        return redirect("profiles:show_self")


class AddWorkExperience(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/add_workexperience.html"
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile_form = forms.ProfileForm(request.POST,
                                         instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "Profile details saved!")
        return redirect("profiles:show_self")


class EditWorkExperience(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_workexperience.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "workexperience_form" not in kwargs:
            slug = request.get_full_path().lstrip('users/me/edit/work/')
            work_experience = get_object_or_404(models.WorkExperience, slug=slug)
            kwargs["workexperience_form"] = forms.WorkExperienceForm(instance=work_experience)
        return super(EditWorkExperience, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        slug = request.get_full_path().lstrip('users/me/edit/work/')
        work_experience = get_object_or_404(models.WorkExperience, slug=slug)
        workexperience_form = forms.WorkExperienceForm(request.POST,
                                                        request.FILES,
                                                        instance=work_experience)
        if not (workexperience_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            workexperience_form = forms.WorkExperienceForm(instance=work_experience)
            return super(EditWorkExperience, self).get(request, workexperience_form=workexperience_form)
        # Form is fine. Time to save!
        workexperience_form.save()
        messages.success(request, "Work experience details saved!")
        return redirect("profiles:show_self")
