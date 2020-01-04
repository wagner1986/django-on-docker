from django.urls import path,re_path
from .views import home

app_name = 'poll'
urlpatterns = [
    re_path(r'^$', home, name='home'),
]