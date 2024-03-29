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
from django.conf.urls import include
from django.contrib import admin
from funmash_app import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

# Class to redirect user to the index page once they
# have completed registration
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/funmash_app/'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^funmash_app/', include('funmash_app.urls')),
    url(r'^accounts/password/change/done/$', views.index, name='index'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
