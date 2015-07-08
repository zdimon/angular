from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, verbose_name='Content')
    topic = models.ForeignKey(Topic, verbose_name='Topic')
