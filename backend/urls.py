from django.conf.urls import url
from . import views

app_name = 'backend'
urlpatterns = [
    url(r'^$', views.index, name='index'), #defalt, api
    url(r'^testdata/', views.testdata, name='testdata'), #sub path, api/testdata
]
