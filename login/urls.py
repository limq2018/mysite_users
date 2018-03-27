from django.conf.urls import url, include
from . import views

app_name = '[login]'
urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^captcha', include('captcha.urls')),
]