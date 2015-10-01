from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class BlogPost(models.Model):
    author = models.ForeignKey(User)
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    title = models.CharField(
        max_length=120
    )
    slug = models.SlugField()
    body = models.TextField()
    image = models.ImageField(upload_to='blogs/images')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return "%s - %s" % (self.title, self.timestamp)


class PostComment(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    post = models.ForeignKey(BlogPost)
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    body = models.TextField()

    def __str__(self):
        return "%s - %s" % (self.author, self.timestamp)
