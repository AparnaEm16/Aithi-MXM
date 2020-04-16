# initial project root app url file
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import  views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/',include('MainApp.urls')), #to access dashboard from root app
    url(r'^signup/',include('accounts.urls')), #to access sign up form 
    url(r'^$',views.home),
]

urlpatterns += staticfiles_urlpatterns()