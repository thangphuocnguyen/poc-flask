"""url config for Blog app."""
from django.conf.urls import url
from . import views


urlpatterns = [
    # Post list
    url(r'^$', views.PostListView.as_view(), name='post_list'),

    # Post detail via canonical url
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),

    # Share the post via email
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
]
