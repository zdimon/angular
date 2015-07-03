    var app = angular.module('AngularApp', [
        'ui.router',
        'restangular'
    ])

    app.config(function ($stateProvider, $urlRouterProvider, RestangularProvider) {
        // For any unmatched url, send to /route1
        $urlRouterProvider.otherwise("/");
        $stateProvider
            .state('index', {

                url: "/",
                templateUrl: "/static/templates/_index.html",
                //controller: "IndexController"
            })

          
    })

   // app.controller("IndexController", ['$scope', 'Restangular', 'CbgenRestangular', '$q',
   // function ($scope, Restangular, CbgenRestangular, $q) {


  //  }])// end controlle
