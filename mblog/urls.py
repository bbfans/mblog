"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from mainsite.views import homepage_blog
from mainsite.views import showpost_blog
from mainsite.views import about_blog
from mainsite.views import cell_index
from mainsite.views import phone_details

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$', homepage_blog),
    url(r'^blog/post/(\w+)$', showpost_blog),
    url(r'^blog/about/', about_blog),
    url(r'', cell_index),
    url(r'^detail/(\d+)$', phone_details, name='detail-url'),
]
