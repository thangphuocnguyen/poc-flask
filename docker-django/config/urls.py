"""djstarter URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls')).
"""
from django.conf.urls import include, url
from django.contrib import admin

from tastypie.api import Api

from apps.accounts.api import UserResource
from apps.notes.api import NoteResource
from apps.issue.api import IssueResource
from apps.blog.api.post_resource import PostResource
from apps.blog.api.comment_resource import CommentResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(IssueResource())
v1_api.register(NoteResource())
v1_api.register(PostResource())
v1_api.register(CommentResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^polls/', include('apps.polls.urls')),
    url(r'^blog/', include(
        'apps.blog.urls',
        namespace='blog',
        app_name='blog'
    )),
    url(r'^api/', include(v1_api.urls)),
]
