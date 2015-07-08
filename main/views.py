from django.shortcuts import render

from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import PageSerializer
from .models import Page

class IndexView(TemplateView):
    template_name = "main/index.html"



class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


