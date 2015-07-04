    var app = angular.module('AngularApp', [
        'ui.router',
        'restangular',
        'app.controllers'
    ]).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

