from django.conf.urls import url

from . import views

app_name = 'mybideo'
urlpatterns = [
    # ex: /mybideo/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /mybideo/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
