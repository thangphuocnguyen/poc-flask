from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS

from .models import Note
from apps.accounts.api import UserResource


class NoteResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Note.objects.all()
        resource_name = 'notes'
        authorization = Authorization()
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
