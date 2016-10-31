from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.shortcuts import render

def forums(request):
        template_name = "forums/forumList.html"
        return render(request, template_name)

#hi there
