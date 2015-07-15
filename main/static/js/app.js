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
})

.run(function ($rootScope, Auth) {

            Auth.isauth(function(result){
                console.log(result);
                if(result.isauth==1) { $rootScope.isAuthenticated = true;  } else { $rootScope.isAuthenticated = false;}
            })

})

