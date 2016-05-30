from django.conf.urls import url, include
from .api import NoteResource

note_resource = NoteResource()

urlpatterns = [
    url(r'^api/', include(note_resource.urls)),
]
