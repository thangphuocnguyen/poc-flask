from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication

from tastypie.utils import trailing_slash

from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
# from django.http import HttpGone, HttpMultipleChoices


from apps.accounts.api import UserResource

from apps.blog.models import Post
from .comment_resource import CommentResource


class PostResource(ModelResource):
    user = fields.ForeignKey(UserResource,
                             'user',
                             full=True,
                             null=True,
                             readonly=True)

    comments = fields.ToManyField("apps.blog.api.comment_resource.CommentRes \
                                  ource",
                                  'comments',
                                  full=True,
                                  null=True)

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        always_return_data = True

    def hydrate(self, bundle, request=None):

        print('here')
        bundle.obj.user = bundle.request.user
        return bundle

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/children%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_children'),
                name="api_get_children"),
        ]

    def get_children(self, request, **kwargs):
        try:
            bundle = self.build_bundle(data={'pk': kwargs['pk']},
                                       request=request)
            obj = self.cached_obj_get(bundle=bundle,
                                      **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()

        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is \
                found at this URI.")

        child_resource = CommentResource()
        return child_resource.get_list(request, parent_id=obj.pk)
