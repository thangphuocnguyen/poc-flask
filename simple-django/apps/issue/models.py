"""Issues."""
from django.db import models
from apps.accounts.models import User


class Issue(models.Model):
    """Define attribute for Issue."""

    user = models.ForeignKey(User, related_name='issue')
    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish'
    )
    content = models.TextField()

    def __str__(self):
        return self.title
