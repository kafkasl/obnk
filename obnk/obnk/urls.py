"""obnk URL Configuration

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
from obnk_apps.users import urls as user_urls
from obnk_apps.financials import urls as financials_urls


urlpatterns = [
    url(r'^v1/users/', include(user_urls)),
    url(r'^v1/financials/', include(financials_urls)),
    url(r'^admin/', admin.site.urls),
]

admin.site.site_header = 'OBnk admin'
