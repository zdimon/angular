# -*- coding: utf-8 -*-
import logging
from django.core.management.base import BaseCommand
from blog.models import Topic, Post



class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'start'
        t = Topic()
        t.name = 'Angular'
        t.save()
        for i in range(0,10):
            p = Post()
            p.topic = t
            p.title = 'First post %s' % i
            p.content = 'Content of the first post'
            p.save()

        t = Topic()
        t.name = 'Python'
        t.save()
        for i in range(0,20):
            p = Post()
            p.topic = t
            p.title = 'Second post %s ' % i
            p.content = 'Content of the second post'
            p.save()

        
        print 'done'

