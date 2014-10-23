from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^level/(?P<level>\d+)$', 'treasure_hunt.views.display_level', name='level_url'),
    url(r'^leaderboard/', 'treasure_hunt.views.display_leaderboard'),
    url(r'', 'treasure_hunt.views.index', name='index'),
)
