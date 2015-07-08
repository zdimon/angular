from django.contrib import admin
from .models import Topic, Post

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Topic, TopicAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'content')

admin.site.register(Post, PostAdmin)

