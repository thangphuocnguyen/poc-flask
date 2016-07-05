from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication

from apps.accounts.api import UserResource

from apps.blog.models import Post
from .comment_resource import CommentResource


class PostResource(ModelResource):
    user = fields.ForeignKey(UserResource,
                             'user',
                             full=True,
                             null=True,
                             readonly=True)

    comments = fields.ToManyField(CommentResource, 'comments', full=True)

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        always_return_data = True

    def hydrate(self, bundle, request=None):
        bundle.obj.user = bundle.request.user
        return bundle
