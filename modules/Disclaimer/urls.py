from django.conf.urls import url
from .views import Index, lista_Sitiosxregion

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', Index, name='index-disclaimer'),
    url(r'^region/(?P<region>[\w-]+)/$', lista_Sitiosxregion, name='sitios_por_region'),
]