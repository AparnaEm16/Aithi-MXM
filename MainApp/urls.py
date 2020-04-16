# Main App url file
from django.conf.urls import url
from . import  views
urlpatterns = [
    url(r'^$',views.dashboard) , #url for  dashboard
]

