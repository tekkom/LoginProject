from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'newsfeed/', views.index, name='events'),
]
