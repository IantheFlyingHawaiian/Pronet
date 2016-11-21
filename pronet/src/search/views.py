from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.shortcuts import render
from profiles import models

class Search(generic.TemplateView):
    def get(self, request):
        template_premium = "search/search_premium.html"
        template_nonpremium = "search/search_nonpremium.html"

        currentuser = self.request.user
        queryset = models.Profile.objects.all()
        queryset_work = models.WorkExperience.objects.all()

        exists = models.Profile.objects.filter(user=currentuser, premium_flag=True).exists()

        npquery = request.GET.get("np-search")
        if npquery:
            queryset = queryset.filter(user__name__icontains=npquery)

        pquery_name = request.GET.get("search")
        if pquery_name:
            queryset = queryset.filter(user__name__icontains=pquery_name)

        pquery_degree = request.GET.get("deg")
        if pquery_degree:
            queryset = queryset.filter(degree__icontains=pquery_degree)

        '''
        pquery_school = request.GET.get("schl")
        if pquery_school:
            queryset = queryset.filter(user__name__icontains=pquery_school)

        pquery_level = request.GET.get("edu")
        if pquery_level:
            queryset = queryset.filter(user__name__icontains=pquery_level)
        '''

        '''
        pquery_skill = request.GET.get("skill")
        if pquery_skill:
            queryset = queryset.filter(user__name__icontains=pquery_skill)

        pquery_years = request.GET.get("yskill")
        if pquery_years:
            queryset = queryset.filter(user__name__icontains=pquery_years)
        '''

        pquery_ywork = request.GET.get("ywork")
        if pquery_ywork:
            queryset = queryset.filter(work_years__icontains=pquery_ywork)

        '''
        pquery_company = request.GET.get("cmpy")
        if pquery_company:
            queryset_work = queryset_work.filter(company__icontains=pquery_company)
        '''

        if exists:
            return render(request, template_premium, {'users': queryset, 'currentuser':currentuser})
        else:
            return render(request, template_nonpremium, {'users': queryset, 'currentuser':currentuser})