from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^hello/', 'myapp.views.hello', name = 'hello'),
]
