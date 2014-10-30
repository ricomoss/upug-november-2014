from django.conf.urls import patterns, url

from example_app import views


urlpatterns = patterns('',
    url(r'^$', views.FibNum.as_view(), name='fib_num')
)
