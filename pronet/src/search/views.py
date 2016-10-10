from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.shortcuts import render
from profiles import models


def search(request):
    template_name = "search/search_it.html"
    users = models.Profile.objects.all()
    context = {'users': users}
    return render(request, template_name, context)
    '''
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
    template = loader.get_template('search/search_it.html')
    context = { 'users':users }

    print(context)
    return HttpResponse(template.render(context, request))
    '''