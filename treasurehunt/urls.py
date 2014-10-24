from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^treasurehunt/', include('treasure_hunt.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'treasurehunt.views.index'),
    url(r'', include('registration.backends.default.urls'))
) 



