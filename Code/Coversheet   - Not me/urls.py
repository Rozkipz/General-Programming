from django.conf.urls import url,patterns,include
from . import views

#urlpatterns = patterns(
    #url(r'^$', include('views.index'), name='index'),
    #url(r'^$', include('views.post_list'), name='post_list'),
    #url(r'^post/(?P<pk>\d+)/$', include('views.post_detail'), name='post_detail'),
    #url(r'^postnew/', views.postnew, name="postnew"),
#)

# Searches made for any url patterns results in a call to the postnew function within views.py

urlpatterns = [
    url(r'^$', views.postnew),
]