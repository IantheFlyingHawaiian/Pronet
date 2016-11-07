from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^SearchName$', views.Search.as_view(), name='search'),
    url(r'^SearchYears$', views.SearchYears.as_view(), name='searchyears'),
]