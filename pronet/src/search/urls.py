from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^SearchName$', views.Search.as_view(), name='search'),
]