from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),
        name='show'),
    url(r'^me/add/work$', views.AddWorkExperience.as_view(), name='add_work_self'),
    url(r'^me/edit/work/(?P<slug>[\w\-]+)$', views.EditWorkExperience.as_view(), name='edit_work_self'),
]
