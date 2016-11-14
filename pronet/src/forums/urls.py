from django.conf.urls import  url
from . import views

urlpatterns =[
    # ex: /forums/
    url(r'^$', views.forums, name='forums'),
    # ex: /forums/index
    url(r'^index$', views.index, name='index'),
    # ex: /forums/1/
    url(r'^(?P<topic_id>[0-9]+)/$', views.topic, name='topic'),
    # ex: /forums/design/3/
    #url(r'^(?P<topic_id>[0-9]+)/(?P<question_id>[0-9]+)/$', views.questions, name='questions'),
]