from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^coversheet/', include('Coversheet.urls')),
    url(r'^tutormodule/', include('tutormodule.urls')),
    url(r'^uploadsystem', include('fileupload.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('homepage.urls')),
    
]
urlpatterns += staticfiles_urlpatterns()
