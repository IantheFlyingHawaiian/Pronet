from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.shortcuts import render
from profiles import models

class Search(generic.TemplateView):
    def get(self, request):
        template_name = "search/search_username.html"
        users = models.Profile.objects.all()
        return render(request, template_name, {'users': users})

class SearchYears(generic.TemplateView):
    def get(self, request):
        template_name = "search/search_yearsExp.html"
        users = models.Profile.objects.all()
        return render(request, template_name, {'users': users})


'''
    template_name = 'search/search_username.html'

    def get(self, request, *args, **kwargs):
        users = models.Profile.objects.all()
        return render(request, self.template_name, {'user': users})


    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {'user': users})
'''

'''
    template_name = "search/search_username.html"
    http_method_names = ['get']

    def get(self, request, context=None):
        context = context or {}
        context[0] = models.Profile.objects.all()

        return super(Search, self).get(request, context=context)

    def search(request):
        template_name = "search/search_username.html"


        return render(request, template_name, {'users': users})








    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
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

class SearchYears():
    def searchyears(request):
        template_name = "search/search_yearsExp.html"
        users = models.Profile.objects.all()

        return render(request, template_name, {'users': users})

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

    users = models.Profile.objects.all()
    template = loader.get_template('search/search_username.html')
    context = { 'users':users }

    print(context)

    '''