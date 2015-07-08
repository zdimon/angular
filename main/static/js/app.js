    var app = angular.module('AngularApp', [
        'ui.router',
        'restangular',
        'app.controllers',
        'djangoRESTResources',
        'ngCookies',
        'ngSanitize',
    ]).config(function($interpolateProvider,$httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

