from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL

from django.conf.urls import url

from .models import User


class UserResource(ModelResource):
    """
    Endpoint of user.

    Accept: application/json
    Content-Type: application/json

    As a header
    Format is : Authorization: <api_key>
        Authorization: 53xxxxxxxxxxxxxxxxxxxxxxxxxed5d
    """

    class Meta:

        queryset = User.objects.all()
        resource_name = 'users'
        list_allowed_methods = ['get']
        allowed_methods = ['get', 'post', 'put']

        authentication = ApiKeyAuthentication()
        authorization = Authorization()

        include_resource_uri = False
        include_absolute_url = True

        always_return_data = True
        excludes = ['is_staff', 'date_joined', 'is_superuser',
                    'last_login', 'password']

        filtering = {
            'username': ALL,
        }

        custom_filtering = {
            'offset': {
                'dataType': 'int',
                'required': False,
                'description': 'Specify the offset to start displaying' +
                ' element on a page. Default = 0'
            },
            'limit': {
                'dataType': 'int',
                'required': False,
                'description': 'Specify the number of element to display per' +
                ' page. Default = 15'
            },
        }

        extra_actions = [

        ]

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<username>[\w\d_.-]+)/$" %
                self._meta.resource_name,
                self.wrap_view('dispatch_detail'),
                name="api_dispatch_detail"),
        ]
