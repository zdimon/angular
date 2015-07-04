# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import RequestFactory
from djangular.core.urlresolvers import get_all_remote_methods, get_current_remote_methods
from .urls import RemoteMethodsView


class TemplateRemoteMethods(TestCase):
    urls = 'server.tests.urls'

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_current_remote_methods(self):
        view = RemoteMethodsView()
        view.request = self.factory.get('/straight_methods/')
        remote_methods = get_current_remote_methods(view)
        self.assertDictEqual({'foo': {'url': '/straight_methods/', 'headers': {'DjNg-Remote-Method': 'foo'}, 'method': 'auto'}, 'bar': {'url': '/straight_methods/', 'headers': {'DjNg-Remote-Method': 'bar'}, 'method': 'auto'}},
                             remote_methods)

    def test_get_all_remote_methods(self):
        remote_methods = get_all_remote_methods()
        self.assertDictEqual(remote_methods, {'urlresolvertags': {'blah': {u'url': '/url_resolvers/', u'headers': {u'DjNg-Remote-Method': 'blah'}, u'method': 'auto'}}, 'submethods': {'sub': {'app': {'foo': {u'url': '/sub_methods/sub/app/', u'headers': {u'DjNg-Remote-Method': 'foo'}, u'method': 'auto'}, 'bar': {u'url': '/sub_methods/sub/app/', u'headers': {u'DjNg-Remote-Method': 'bar'}, u'method': 'auto'}}}}})
