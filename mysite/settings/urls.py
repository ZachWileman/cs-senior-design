from django.conf.urls import url, include
from settings import views


app_name = 'settings'

urlpatterns = [
    url(r'^$', views.SettingsView.as_view(), name='settings-page'),
    url('add_attack/$', views.SubmitAttackView.as_view(), name='attack-view'),
]
