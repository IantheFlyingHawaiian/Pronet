from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^me/connections$', views.ShowConnections.as_view(), name='show_connections'),
    url(r'^me/connections/(?P<slug>[\w\-]+)/accept$', views.accept_from_page, name='page_accept'),
    url(r'^me/connections/(?P<slug>[\w\-]+)/deny$', views.deny_from_page, name='page_deny'),
    url(r'^me/connections/(?P<slug>[\w\-]+)/revoke$', views.revoke_from_page, name='page_revoke'),
    url(r'^me/connections/(?P<slug>[\w\-]+)/remove$', views.remove_from_page, name='page_remove'),
    url(r'^me/work/add$', views.AddWorkExperience.as_view(), name='add_work_self'),
    url(r'^me/work/edit\/(?P<slug>[\w\-]+)$', views.EditWorkExperience.as_view(), name='edit_work_self'),
    url(r'^me/work/delete\/(?P<slug>[\w\-]+)$', views.DeleteWorkExperience.as_view(), name='delete_work_self'),
    url(r'^me/skill/add$', views.AddSkillExperience.as_view(), name='add_skill_self'),
    url(r'^me/skill/edit\/(?P<slug>[\w\-]+)$', views.EditSkillExperience.as_view(), name='edit_skill_self'),
    url(r'^me/skill/delete\/(?P<slug>[\w\-]+)$', views.DeleteSkillExperience.as_view(), name='delete_skill_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(), name='show'),
    url(r'^(?P<slug>[\w\-]+)/connect$', views.connect, name='connect'),
    url(r'^(?P<slug>[\w\-]+)/accept$', views.accept_from_profile, name='accept'),
    url(r'^(?P<slug>[\w\-]+)/deny$', views.deny_from_profile, name='deny'),
    url(r'^(?P<slug>[\w\-]+)/revoke$', views.revoke_from_profile, name='revoke'),
    url(r'^(?P<slug>[\w\-]+)/remove$', views.remove_from_profile, name='remove'),
]