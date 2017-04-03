from django.conf.urls import url
from .views import Index

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', Index, name='index-disclaimer'),
]