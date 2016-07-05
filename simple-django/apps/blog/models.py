from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

from apps.accounts.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(
            PublishedManager,
            self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    user = models.ForeignKey(User, related_name='blog_posts')

    title = models.CharField(max_length=250)
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    tags = TaggableManager()

    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish'
    )

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return the canonical URL of the object."""
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.strftime('%m'),
                self.publish.strftime('%d'),
                self.slug
            ]
        )

    def save(self, *args, **kwargs):

        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:250]

        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    """Comment for post."""

    # user = models.ForeignKey(User,)
    post = models.ForeignKey(Post, related_name='comments')

    # name = models.CharField(max_length=80)
    # email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format("users", self.post)
