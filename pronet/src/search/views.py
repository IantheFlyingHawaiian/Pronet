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
        exists = models.Profile.objects.filter(user=currentuser, premium_flag=True).exists()

        if exists:
            return render(request, template_premium, {'users': queryset, 'cuurentuser':currentuser})
        else:
            return render(request, template_nonpremium, {'users': queryset, 'cuurentuser':currentuser})