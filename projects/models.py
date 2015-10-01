from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Project(models.Model):
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    title = models.CharField(
        max_length=120
    )
    slug = models.SlugField()
    description = models.TextField()
    blurb = models.CharField(
        max_length=500
    )
    image = models.ImageField(
        upload_to='projects/img'
    )
    link = models.URLField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectComments(models.Model):
    project = models.ForeignKey(Project)
    author = models.ForeignKey(User, blank=True, null=True)
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    body = models.TextField()

    def __str__(self):
        return "%s - %s" % (self.author, self.timestamp)