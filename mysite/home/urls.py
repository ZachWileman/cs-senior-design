from django.conf.urls import url, include
from home import views


app_name = 'home'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='homepage'),
]
