
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource

from .models import Issue
from apps.accounts.api import UserResource


class IssueResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user', full=True, null=True, readonly=True)

    class Meta:
        queryset = Issue.objects.all()
        resource_name = 'issues'
        authorization = Authorization()
        authentication = Authentication()

    def hydrate(self, bundle, request=None):
        print(self)
        print('-----')
        print(bundle)

        import pdb
        pdb.set_trace()

        bundle.obj.user = bundle.request.user
        return bundle
