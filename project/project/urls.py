from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/', 'catalog.views.catalog', name='catalog'),
    url(r'^ajax/parse/', 'home.views.parse', name='parse'),
    url(r'^$', 'home.views.home', name='home')
]
