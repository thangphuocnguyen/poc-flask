# flavors/models.py
from django.core.urlresolvers import reverse
from django.db import models

STATUS = (
    (0, "zero"),
    (1, "one"),
)


class Flavor(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    scoops_remaining = models.IntegerField(default=0, choice=STATUS)

    def get_absolute_url(self):
        return reverse("flavors:detail", kwargs={"slug": self.slug})
