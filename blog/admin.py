from django.contrib import admin
from .models import BlogPost, PostComment


class BlogPostAdmin(admin.ModelAdmin):
    exclude = [
        'slug'
    ]

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(PostComment)


