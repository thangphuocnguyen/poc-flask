from tastypie.utils.timezone import now
# from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from apps.accounts.models import User


class Note(models.Model):
    """Model for a Note."""

    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    body = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Note, self).save(*args, **kwargs)
