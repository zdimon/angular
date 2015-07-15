"""angular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from authentication.views import AuthView

from rest_framework import routers, serializers, viewsets
from main.views import IndexView, PageViewSet
from blog.views import PostViewSet, TopicViewSet, ToicPostsList, CommentPostsList, CommentFormView, CommentViewSet

router = routers.DefaultRouter()
router.register(r'page', PageViewSet)
router.register(r'post', PostViewSet)
router.register(r'topic', TopicViewSet)
router.register(r'comment', CommentViewSet)


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^auth/$', AuthView.as_view(), name='auth'),

    #######API##############
    url(r'^api/login/$', 'authentication.views.login_user'),
    url(r'^api/logout/$', 'authentication.views.logout'),
    url(r'^api/isauth/$', 'authentication.views.isauth'),
    url(r'^registration/$', 'authentication.views.registration'),
    #########################

    url(r'^api/', include(router.urls)),

    #############BLOG####################
    url(r'^api/posts/(?P<topic_id>\d+)$', ToicPostsList.as_view()),
    url(r'^api/comment/(?P<post_id>\d+)$', CommentPostsList.as_view()),
    url(r'^api/comments/form$', CommentFormView.as_view()),
    #####################################
    
    url(r'^admin/', include(admin.site.urls)),
]
