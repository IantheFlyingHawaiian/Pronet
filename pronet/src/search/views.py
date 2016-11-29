from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.shortcuts import render
from django.db.models import Q
from itertools import chain
import itertools
from profiles import models
from decimal import Decimal

class Search(generic.TemplateView):
   def get(self, request):
       template_premium = "search/search_premium.html"
       template_nonpremium = "search/search_nonpremium.html"

       currentuser = self.request.user
       queryset_work = models.WorkExperience.objects.all()
       queryset_skill = models.SkillExperience.objects.all()
       queryset_education = models.University.objects.all()
       queryset = None

       exists = models.Profile.objects.filter(user=currentuser, premium_flag=True).exists()

       #username search
       npquery = request.GET.get("npsearch")
       if npquery:
           queryset = models.Profile.objects.all()
           queryset = queryset.filter(Q(user__name__icontains=npquery))

       #SEARCH by EDUCATION
       pquery_degree = request.GET.get("degree")
       if npquery == None:
           if pquery_degree:
               queryset = models.Profile.objects.all()
               queryset = queryset.filter(Q(degree__icontains=pquery_degree))

       #SEARCH by SKILLS
       pquery_skill = request.GET.get("skill")
       pquery_years = request.GET.get("yskill")
       if npquery == None and pquery_degree == None:

           if queryset_skill != None or pquery_years != 0:
               if pquery_years:
                   pquery_years = Decimal(pquery_years)

               if pquery_skill != None and pquery_years != 0:
                   queryset_skill = queryset_skill.filter(Q(skill_name__icontains=pquery_skill) &
                                                Q(skill_years__gte=pquery_years))

               if pquery_skill != None and pquery_years == 0:
                   queryset_skill = queryset_skill.filter(Q(skill_name__icontains=pquery_skill))

               queryset = models.Profile.objects.all()

               for user in queryset_skill:
                   queryset = queryset.filter(user__profile=user.profile)


       #SEARCH by WORK EXPERIENCE
       pquery_yearWorkExp = request.GET.get("ywork")
       pquery_company = request.GET.get("cmpy")
       if npquery == None and pquery_degree == None and pquery_skill == None and pquery_years == None:
           if pquery_yearWorkExp:
                pquery_yearWorkExp = Decimal(pquery_yearWorkExp)

           if pquery_company != None and pquery_yearWorkExp != 0:
               queryset_work = queryset_work.filter(Q(company__icontains=pquery_company))#include pquery_yearWorkExp

           if pquery_company != None and pquery_yearWorkExp == 0:
               queryset_work = queryset_work.filter(Q(company__icontains=pquery_company))

           queryset = models.Profile.objects.all()

           for user in queryset_work:
               queryset = queryset.filter(user__profile=user.profile)

       if exists:
           return render(request, template_premium, {'users': queryset, 'currentuser': currentuser})
       else:
           return render(request, template_nonpremium, {'users': queryset, 'currentuser': currentuser})
