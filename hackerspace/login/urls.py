from django.conf.urls import url
from . import views


app_name = 'login'

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^validate', views.validate, name='validate'),
    url(r'^register', views.register, name='register'),
]
