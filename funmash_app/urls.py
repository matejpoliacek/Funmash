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
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/(?P<image_name>[\d+]+)/$', views.index, name='index'),
    url(r'^liked_images/$', views.like_picture, name='liked_images'),
    url(r'^render_pic1/$', views.render_pic1, name='render_pic1'),
    url(r'^render_pic2/$', views.render_pic2, name='render_pic2'),
    url(r'^about/$', views.about, name='about'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^uploaded/$', views.uploaded, name='uploaded'),
    url(r'^top5/$', views.top5, name='top5'),
]

