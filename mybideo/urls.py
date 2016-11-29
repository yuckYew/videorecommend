from django.conf.urls import url

from . import views

app_name = 'mybideo'
urlpatterns = [
    # ex: /mybideo/
    url(r'^$', views.index, name='index'),
    # ex: /mybideo/5/
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
]
