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
                controller: function($scope, Restangular,TopicResource) {
                    $scope.items = ["A", "List", "Of", "Items"];
                    var baseAccounts = Restangular.all('accounts');
                    //baseAccounts.getList().then(function(accounts) {
                    //  $scope.allAccounts = accounts;
                    //});
                  }
            })
            .state('register', {
                url: "/register",
                templateUrl: "/static/templates/registration/register.html",
                controller: function($scope,djangoAuth) {
                    return djangoAuth.authenticationStatus();
                  }
            })


            .state('page', {
                url: "/page/:id",
                templateUrl: "/static/templates/_page.html",
                controller: function($scope, Restangular, $stateParams, PageResource) {
                        var page = PageResource.get({id:$stateParams.id}, function() {
                            $scope.page = page;
                        });                       
                  }
                })

            .state('topic', {
                url: "/topic/:id/page/:page",
                templateUrl: "/static/templates/_topic.html",
                controller: function($scope, Restangular, $stateParams, TopicResource, PostsResource) {
                        var topic = TopicResource.get({id:$stateParams.id}, function() {
                            $scope.topic = topic;
                            PostsResource.posts(topic.id,$stateParams.page).success(function(result) {
                                $scope.posts = result;
                                console.log($stateParams.page);
                            });
                        });                       
                  }
                })   

            .state('post', {
                url: "/post/:id/page/:page",
                templateUrl: "/static/templates/_post.html",
                controller: function($scope, Restangular, $stateParams, TopicResource, PostResource, CommentListResource) {
                        var post = PostResource.get({id:$stateParams.id}, function() {
                            $scope.post = post;
                            
                        });                       
                  }
                })         
         


    
  }

})();

