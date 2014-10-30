from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^fib-num/$', include('example_app.urls')),
)
