(function () {
  'use strict';

  angular
    .module('AngularApp')
    .config(config);

  function config($urlRouterProvider, $stateProvider) {
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
                    
                    //$scope.items = ["A", "List", "Of", "Items"];
                    //var baseAccounts = Restangular.all('accounts');
                    //baseAccounts.getList().then(function(accounts) {
                    //  $scope.allAccounts = accounts;
                    //});
                  }
            });
    
  }

})();

