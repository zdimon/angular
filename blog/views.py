from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, TopicSerializer, CommentSerializer
from .models import Post, Topic, Comment
from rest_framework import generics


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ToicPostsList(generics.ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        topic = Topic.objects.get(pk = self.kwargs['topic_id'])
        return Post.objects.filter(topic=topic)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class CommentPostsList(generics.ListAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        post = Post.objects.get(pk = self.kwargs['post_id'])
        return Comment.objects.filter(post=post)


