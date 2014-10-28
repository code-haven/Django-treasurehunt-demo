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
    url(r'', include('registration.backends.simple.urls'))
) 

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )



