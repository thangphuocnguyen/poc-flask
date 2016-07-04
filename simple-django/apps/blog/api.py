from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication

from .models import Post
from apps.accounts.api import UserResource


class PostResource(ModelResource):
    user = fields.ForeignKey(UserResource,
                             'user',
                             full=True,
                             null=True,
                             readonly=True)

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        always_return_data = True


    def hydrate(self, bundle, request=None):
        bundle.obj.user = bundle.request.user
        return bundle


class PostsByUserResource(ModelResource):
    """Allow GET posts that user owned."""

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        always_return_data = True


    def hydrate(self, bundle, request=None):
        bundle.obj.user = bundle.request.user
        return bundle
