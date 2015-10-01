from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^$',
        views.All.as_view(),
        name='all',
    ),
    url(
        r'^(?P<slug>[a-z0-9-_]+)/$',
        views.SinglePost.as_view(),
        name='single_post'
    )
]
