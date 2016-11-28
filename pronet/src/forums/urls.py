from django.conf.urls import  url
from . import views

urlpatterns =[
    # ex: /forums/
    url(r'^$', views.forums, name='forums'),
    # ex: /forums/index
    url(r'^index$', views.index, name='index'),
    # ex: /forums/1/
    url(r'^(?P<topic_text>[a-zA-Z0-9]+)/$', views.topic, name='topic'),
    # ex: /forums/design/1/
    url(r'^(?P<topic_id>[a-zA-Z0-9]+)/(?P<question_id>[0-9]+)/$', views.questions, name='questions'),
    # ex: /forums/design/newQuestion
    url(r'^(?P<topic_id>[a-zA-Z0-9]+)/newQuestion/$', views.question_new, name='question_new'),
    url(r'^(?P<topic_id>[a-zA-Z0-9]+)/(?P<question_id>[\w\Wa-zA-Z0-9]+)/newAnswer/$', views.add_answer_to_question, name='add_answer_to_question'),

]