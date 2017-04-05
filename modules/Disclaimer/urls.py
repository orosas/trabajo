from django.conf.urls import url
from .views import Index, Sitiosxregion

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', Index, name='index-disclaimer'),
    url(r'^region/(?P<region>[\w-]+)/$', Sitiosxregion, name='sitios_por_region'),
]