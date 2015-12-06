from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    'home.views',
    url(r'^$/', views.home, name='home'),
)