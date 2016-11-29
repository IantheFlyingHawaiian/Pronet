from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.forms.models import formset_factory
from django.urls import reverse_lazy
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

        # Get connection info, or lack of it
        current_user = request.user
        try:
            connection = models.Connection.objects.get(profile1=current_user.profile, profile2=user.profile)
            kwargs["connection"] = connection
        except ObjectDoesNotExist:
            try:
                connection = models.Connection.objects.get(profile1=user.profile, profile2=current_user.profile)
                kwargs["connection"] = connection
            except ObjectDoesNotExist:
                kwargs["connection"] = False

        return super(ShowProfile, self).get(request, *args, **kwargs)


def connect(request, slug):
    current_user = request.user.profile
    other_user = get_object_or_404(models.Profile, slug=slug)

    conn = models.Connection(profile1=current_user, profile2=other_user)
    conn.save()

    return redirect("profiles:show", slug=slug)

def accept_from_profile(request, slug):
    current_user = request.user.profile
    other_user = get_object_or_404(models.Profile, slug=slug)
    conn = get_object_or_404(models.Connection, profile1=other_user, profile2=current_user)

    conn.pending = False
    conn.save()

    return redirect("profiles:show", slug=slug)

def deny_from_profile(request, slug):
    current_user = request.user.profile
    other_user = get_object_or_404(models.Profile, slug=slug)
    conn = get_object_or_404(models.Connection, profile1=other_user, profile2=current_user)

    conn.delete()

    return redirect("profiles:show", slug=slug)

def revoke_from_profile(request, slug):
    current_user = request.user.profile
    other_user = get_object_or_404(models.Profile, slug=slug)
    conn = get_object_or_404(models.Connection, profile1=current_user, profile2=other_user)

    conn.delete()

    return redirect("profiles:show", slug=slug)

def remove_from_profile(request, slug):
    current_user = request.user.profile
    other_user = get_object_or_404(models.Profile, slug=slug)
    if models.Connection.objects.filter(profile1=current_user, profile2=other_user):
        conn = get_object_or_404(models.Connection, profile1=current_user, profile2=other_user)
    else:
        conn = get_object_or_404(models.Connection, profile1=other_user, profile2=current_user)

    conn.delete()

    return redirect("profiles:show", slug=slug)


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
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "workexperience_form" not in kwargs:
            kwargs["workexperience_form"] = forms.AddWorkExperienceForm()
        return super(AddWorkExperience, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        workexperience_form = forms.AddWorkExperienceForm(request.POST)
        if not (workexperience_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            workexperience_form = forms.AddWorkExperienceForm()
            return super(AddWorkExperience, self).get(request, workexperience_form=workexperience_form)
        # Form is fine. Time to save!
        workexperience = workexperience_form.save(commit=False)
        workexperience.profile = user.profile
        workexperience.save()
        messages.success(request, "Work experience details saved!")
        return redirect("profiles:show_self")


class EditWorkExperience(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_workexperience.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "workexperience_form" not in kwargs:
            slug = request.get_full_path().lstrip('users/me/work/edit/')
            work_experience = get_object_or_404(models.WorkExperience, slug=slug)
            kwargs["workexperience_form"] = forms.EditWorkExperienceForm(instance=work_experience)
        return super(EditWorkExperience, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        slug = request.get_full_path().lstrip('/users/me/work/edit/')
        work_experience = get_object_or_404(models.WorkExperience, slug=slug)
        workexperience_form = forms.EditWorkExperienceForm(request.POST,
                                                           request.FILES,
                                                           instance=work_experience)
        if not (workexperience_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            workexperience_form = forms.EditWorkExperienceForm(instance=work_experience)
            return super(EditWorkExperience, self).get(request, workexperience_form=workexperience_form)
        # Form is fine. Time to save!
        workexperience_form.save()
        messages.success(request, "Work experience details saved!")
        return redirect("profiles:show_self")


class DeleteWorkExperience(LoginRequiredMixin, generic.edit.DeleteView):
    template_name = "profiles/delete_workexperience.html"
    model = models.WorkExperience
    success_url = reverse_lazy('profiles:show_self')


class AddSkillExperience(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/add_skill.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "skillexperience_form" not in kwargs:
            kwargs["skillexperience_form"] = forms.AddSkillExperienceForm()
        return super(AddSkillExperience, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        skillexperience_form = forms.AddSkillExperienceForm(request.POST)
        if not (skillexperience_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            skillexperience_form = forms.AddSkillExperienceForm()
            return super(AddSkillExperience, self).get(request, skillexperience_form=skillexperience_form)

        # Form is fine. Time to save!
        skillexperience = skillexperience_form.save(commit=False)
        skillexperience.profile = user.profile
        skillexperience.save()
        messages.success(request, "Skill experience details saved!")
        return redirect("profiles:show_self")


class EditSkillExperience(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_skill.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "skillexperience_form" not in kwargs:
            slug = request.get_full_path().lstrip('users/me/skill/edit/')
            skill_experience = get_object_or_404(models.SkillExperience, slug=slug)
            kwargs["skillexperience_form"] = forms.EditSkillExperienceForm(instance=skill_experience)
        return super(EditSkillExperience, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        slug = request.get_full_path().lstrip('/users/me/skill/edit/')
        skill_experience = get_object_or_404(models.SkillExperience, slug=slug)
        skillexperience_form = forms.EditSkillExperienceForm(request.POST,
                                                           request.FILES,
                                                           instance=skill_experience)
        if not (skillexperience_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            skillexperience_form = forms.EditSkillExperienceForm(instance=skill_experience)
            return super(EditSkillExperience, self).get(request, skillexperience_form=skillexperience_form)
        # Form is fine. Time to save!
        skillexperience_form.save()
        messages.success(request, "Skill experience details saved!")
        return redirect("profiles:show_self")


class DeleteSkillExperience(LoginRequiredMixin, generic.edit.DeleteView):
    template_name = "profiles/delete_skill.html"
    model = models.SkillExperience
    success_url = reverse_lazy('profiles:show_self')


class ShowConnections(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_connections.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        current_profile = current_user.profile

        # Get connection info, or lack of it
        kwargs["completed_connection_list"] = models.Connection.objects.filter(
            (Q(profile1=current_profile) | Q(profile2=current_profile)) & Q(pending=False)
        ).order_by("profile1__user__name", "profile2__user__name")

        kwargs["pending_connection_list"] = models.Connection.objects.filter(
            (Q(profile1=current_profile) | Q(profile2=current_profile)) & Q(pending=True)
        ).order_by("profile1__user__name", "profile2__user__name")

        return super(ShowConnections, self).get(request, *args, **kwargs)


def accept_from_page(request, slug):
    current_user = request.user.profile
    other_user = get_object_or_404(models.Profile, slug=slug)
    conn = get_object_or_404(models.Connection, profile1=other_user, profile2=current_user)

    conn.pending = False
    conn.save()

    return redirect("profiles:show_connections")

def deny_from_page(request, slug):
    current_user = request.user.profile
    other_user = get_object_or_404(models.Profile, slug=slug)
    conn = get_object_or_404(models.Connection, profile1=other_user, profile2=current_user)

    conn.delete()

    return redirect("profiles:show_connections")

def revoke_from_page(request, slug):
    current_user = request.user.profile
    other_user = get_object_or_404(models.Profile, slug=slug)
    conn = get_object_or_404(models.Connection, profile1=current_user, profile2=other_user)

    conn.delete()

    return redirect("profiles:show_connections")

def remove_from_page(request, slug):
    current_user = request.user.profile
    other_user = get_object_or_404(models.Profile, slug=slug)
    if models.Connection.objects.filter(profile1=current_user, profile2=other_user):
        conn = get_object_or_404(models.Connection, profile1=current_user, profile2=other_user)
    else:
        conn = get_object_or_404(models.Connection, profile1=other_user, profile2=current_user)

    conn.delete()

    return redirect("profiles:show_connections")