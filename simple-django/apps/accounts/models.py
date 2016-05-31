from django.db import models
from django.contrib.auth.models import AbstractUser

from tastypie.models import create_api_key


###############################################################################
# This class extend User model
###############################################################################
class User(AbstractUser):
    """
    Model to represent User info
    """
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.username

# Make API-KEY for user
models.signals.post_save.connect(create_api_key, sender=User)
