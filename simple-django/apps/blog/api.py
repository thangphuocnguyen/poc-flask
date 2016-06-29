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

    # def obj_create(self, bundle, **kwargs):
    #     bundle.data['user'] = {'pk': bundle.request.user.pk}
    #     return super(PostResource, self).obj_create(bundle, **kwargs)
