from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'user',
        'publish',
        'status',
        'get_absolute_url'
    )

    list_filter = ('status', 'created', 'publish', 'user')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
