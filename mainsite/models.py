from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Blog(models.Model):

    PUBLISH_CHOICES = ((1, "Published"),
                       (2, "Draft")
                       )

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    opening_content = models.TextField()
    extended_content = models.TextField(blank=True, null=True)
    published = models.IntegerField(choices=PUBLISH_CHOICES, default=2)
    publish_date = models.DateField(db_index=True, auto_now_add=True)

    def full_content(self):
        return self.opening_content + self.extended_content