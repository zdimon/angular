    var app = angular.module('AngularApp', [
        'ui.router',
        'restangular'
    ])

    app.config(function ($stateProvider, $routeProvider, $urlRouterProvider,  RestangularProvider) {
        // For any unmatched url, send to /route1
        $urlRouterProvider.otherwise("/");

     

        $stateProvider
            .state('index', {

                url: "/",
                templateUrl: "/static/templates/_index.html",
                controller: function($scope, Restangular) {
                    $scope.items = ["A", "List", "Of", "Items"];
                    var baseAccounts = Restangular.all('accounts');
                    //baseAccounts.getList().then(function(accounts) {
                    //  $scope.allAccounts = accounts;
                    //});
                  }
            })
            .state('register', {

                url: "/register",
                templateUrl: "/static/templates/_registration.html",
                controller: function($scope, Restangular) {
                    $scope.items = ["A", "List", "Of", "Items"];
                    var baseAccounts = Restangular.all('accounts');
                    //baseAccounts.getList().then(function(accounts) {
                    //  $scope.allAccounts = accounts;
                    //});
                  }
            });


        

          
    })
    .controller('RegistrationController', ['$scope', function($scope) {
      $scope.list = [];
      $scope.text = 'hello';
      $scope.submit = function() {
        
          alert($scope.email) ;
        
      };
    }]);

   // app.controller("IndexController", ['$scope', 'Restangular', 'CbgenRestangular', '$q',
   // function ($scope, Restangular, CbgenRestangular, $q) {


  //  }])// end controlle
