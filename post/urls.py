from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('post.views',
    url(r'^$', 'hello_world', {}, name='hello-world'),
)
