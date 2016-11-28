from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.shortcuts import render
from django.db.models import Q
import sys
from profiles import models

class Search(generic.TemplateView):
    def get(self, request):
        template_premium = "search/search_premium.html"
        template_nonpremium = "search/search_nonpremium.html"

        currentuser = self.request.user
        queryset_work = models.WorkExperience.objects.all()
        queryset = None
        exists = models.Profile.objects.filter(user=currentuser, premium_flag=True).exists()

        #username search
        npquery = request.GET.get("npsearch")
        if npquery:
            queryset = models.Profile.objects.all()
            queryset = queryset.filter(Q(user__name__icontains=npquery))


        #SEARCH by EDUCATION
        pquery_degree = request.GET.get("deg")
        pquery_school = request.GET.get("schl")
        if pquery_degree:
            queryset = models.Profile.objects.all()
            queryset = queryset.filter(Q(degree__icontains=pquery_degree))

        '''pquery_school = request.GET.get("schl")
        if pquery_school:
            queryset = models.Profile.objects.all()
            queryset = queryset.filter(school__icontains=pquery_school)

        pquery_level = request.GET.get("eduLevel")
        if pquery_level:
            queryset = models.Profile.objects.all()
            queryset = queryset.filter(user__name__icontains=pquery_level)

        #SEARCH by SKILLS
        pquery_skill = request.GET.get("skill")
        if pquery_skill:
            queryset = models.Profile.objects.all()
            queryset = queryset.filter(user__name__icontains=pquery_skill)

        pquery_years = request.GET.get("yskill")
        if pquery_years:
            queryset = queryset.filter(user__name__gte=pquery_years)

        #SEARCH by WORK EXPERIENCE
        pquery_ywork = request.GET.get("ywork")
        if pquery_ywork:
            queryset = models.Profile.objects.all()
            #pquery_ywork = int(pquery_ywork)
            queryset = queryset.filter(work_years__gte=pquery_ywork)'''

        pquery_company = request.GET.get("cmpy")
        if pquery_company:
            queryset_work = queryset_work.filter(company__icontains=pquery_company)

        if exists:
            return render(request, template_premium, {'users': queryset, 'currentuser':currentuser})
        else:
            return render(request, template_nonpremium, {'users': queryset, 'currentuser':currentuser})