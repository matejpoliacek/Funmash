"""funmash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from funmash_app import views

# @PETER 
# I didn't put in URLs for account disabled and invalid login
# because they don't have separate views. If you don't like
# that the URL doesn't change, we can make separate
# simple views for these, like the 'logout' view.
# This version is working though and I think it's neater:)
# @PETER

urlpatterns = [
    url(r'^$', views.index, name='index'),
# experimenting with how images are passed - modified urls as well (added index2 view)
    url(r'^index/(?P<image_name>[\d+]+)/$', views.index2, name='index2'),
    url(r'^about/$', views.about, name='about'),
    url(r'^change_password/$', views.change_password, name='change_password'),
  #  url(r'^login/$', views.login, name='login'),
    url(r'^profile/$', views.profile, name='profile'),
 #   url(r'^register/$', views.register, name='register'),
    url(r'^top5/$', views.top5, name='top5'),
   # url(r'^logout/$', views.logout, name='logout'),

]

