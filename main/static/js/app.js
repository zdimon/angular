    var app = angular.module('AngularApp', [
        'ui.router',
        'restangular',
        'app.controllers',
        'djangoRESTResources',
        'ngCookies',
        'ngSanitize',
        'ng.django.forms'
    ]).config(function($interpolateProvider,$httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})

.run(function ($rootScope, Auth) {

            Auth.isauth(function(result){
                console.log(result);
                if(result.isauth==1) { 
                        $rootScope.isAuthenticated = true;  
                        $rootScope.username = result.username;  
                        $rootScope.user_id = result.user_id;  
                    } else { $rootScope.isAuthenticated = false;}
            })

})

