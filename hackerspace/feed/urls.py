from django.conf.urls import url

from . import views

app_name = 'feed'

urlpatterns = [
    url(r'^$',views.feed,name='feed'),
]
