from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^complete/', views.complete),
    url(r'^$', views.getmoduleinfo),
]