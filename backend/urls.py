from django.conf.urls import url
from . import views

app_name = 'backend'
urlpatterns = [
    url(r'^$', views.index, name='index'), #链接示例API
]
