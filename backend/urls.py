from django.conf.urls import url
from . import views

app_name = 'backend'
urlpatterns = [
    url(r'^$', views.index, name='index'), #defalt, api
    url(r'^testdata/', views.testdata, name='testdata'), #api/testdata
    url(r'^teststring/', views.teststring, name='teststring'), #api/teststring
]
