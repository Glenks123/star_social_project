from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    #New feature of django 1.11, auth_views include LoginView and LogoutView
    url(r'^login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    #We are not creating a template name for logout, because the new auth feature automatically takes you to the homepage
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^signup/$',views.SignUp.as_view(),name='signup'),
]
