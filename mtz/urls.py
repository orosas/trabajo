"""mtz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^enrollment', include('modules.Enrollment.urls', namespace='Enrollment', app_name='Enrollment'), name="Enrollment"),
    url(r'^disclaimer/', include('modules.Disclaimer.urls', namespace='Disclaimer', app_name='Disclaimer'), name="Disclaimer"),
    url(r'^$', TemplateView.as_view(template_name='base_gral.html'), name="Inicio"),
]

# Cambia el Título en Django Admin
admin.site.site_header = 'MasTec México Admin'