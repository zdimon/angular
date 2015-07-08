from django.contrib import admin
from .models import Topic, Post, Comment

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Topic, TopicAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'content')

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'post', 'created_at')
    list_filter = ('post',)

admin.site.register(Comment, CommentAdmin)

