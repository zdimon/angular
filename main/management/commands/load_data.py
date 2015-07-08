# -*- coding: utf-8 -*-
import logging
from django.core.management.base import BaseCommand
from main.models import Page



class Command(BaseCommand):

    def handle(self, *args, **options):
        
        print 'start'
        Page.objects.all().delete()
        p = Page.objects.create(title=u'Главная', content=u'Текст на главной странице')
        p = Page.objects.create(title=u'О нас', content=u'Информация о компании')
        p = Page.objects.create(title=u'Контакты', content=u'Контактная информация')
        print 'done'



       
