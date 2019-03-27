"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from two_factor.urls import urlpatterns as tf_urls
from django.conf.urls import url
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls
from two_factor.admin import AdminSiteOTPRequired

admin.site.__class__ = AdminSiteOTPRequired

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(tf_twilio_urls)),
    url(r'', include(tf_urls)),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
