from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User)
    content = models.TextField()
    create = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return self.title


