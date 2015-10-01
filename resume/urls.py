
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import settings

urlpatterns = [
    url(
        r'',
        include(
            'main.urls',
            namespace='main'
        )
    ),
    url(
        r'^blog/',
        include(
            'blog.urls',
            namespace='blog'
        )
    ),
    url(
        r'^projects/',
        include(
            'projects.urls',
            namespace='projects'
        )
    ),
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
