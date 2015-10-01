from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.Home.as_view(),
        name='home'
    ),
    url(
        r'^contact/$',
        views.Contact.as_view(),
        name='contact'
    ),
    url(
        r'^thank_you/$',
        views.ThankYou.as_view(),
        name='thank_you'
    ),
    url(
        r'^about/$',
        views.About.as_view(),
        name='about'
    ),
    url(
        r'^links/$',
        views.Links.as_view(),
        name='links'
    ),
    url(
        r'^info/$',
        views.Info.as_view(),
        name='info'
    )
]
