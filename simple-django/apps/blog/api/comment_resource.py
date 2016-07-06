
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication

from apps.accounts.api import UserResource

from apps.blog.models import Comment
from .post_resource import PostResource


class CommentResource(ModelResource):
    user = fields.ForeignKey(UserResource,
                             'user',
                             full=True,
                             null=True,
                             readonly=True)

    post = fields.ForeignKey(PostResource,
                             'post',
                             full=True,
                             null=True,
                             readonly=True)

    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comments'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        always_return_data = True

    def hydrate(self, bundle, request=None):

        print("here")
        import pdb
        pdb.set_trace()

        bundle.obj.user = bundle.request.user
        return bundle
