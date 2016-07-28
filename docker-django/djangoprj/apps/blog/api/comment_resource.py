
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from djangoprj.apps.accounts.api import UserResource

from djangoprj.apps.blog.models import Comment
# from .post_resource import PostResource

class CommentResource(ModelResource):
    user = fields.ForeignKey(UserResource,
                             'user',
                             full=True,
                             null=True,
                             readonly=True)

    post = fields.ForeignKey("djangoprj.apps.blog.api.post_resource.PostResource",
                             'post',
                             null=True)
    post_id = fields.CharField(attribute='post_id', readonly=True, default="111")

    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comments'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        always_return_data = True
        filtering = {
            "post": ALL,
            "post_id": ALL
        }

    def hydrate(self, bundle, request=None):

        # print("here")
        # import pdb
        # pdb.set_trace()

        bundle.obj.user = bundle.request.user
        return bundle
