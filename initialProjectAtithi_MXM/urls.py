
from django.conf.urls import url
from django.contrib import admin
from . import  views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
]

urlpatterns += staticfiles_urlpatterns()