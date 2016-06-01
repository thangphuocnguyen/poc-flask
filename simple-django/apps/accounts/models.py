from django.db import models
from django.contrib.auth.models import AbstractUser

from tastypie.models import create_api_key


###############################################################################
# This class extend User model
###############################################################################
class User(AbstractUser):
    """Model to represent User info."""

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        """
        Return the canonical URL of the object.

        Just for example with include_absolute_url = True in tastypie api
        """
        # return reverse(
        #     'blog:post_detail',
        #     args=[
        #         self.publish.year,
        #         self.publish.strftime('%m'),
        #         self.publish.strftime('%d'),
        #         self.slug
        #     ]
        # )

        return ('Name: {user.username}, Birthday: {user.date_of_birth},' +
                ' Last: {user.last_name}').format(user=self)

# Make API-KEY for user
models.signals.post_save.connect(create_api_key, sender=User)
