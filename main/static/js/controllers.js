angular.module('app.controllers', [])
    
    .controller('RegistrationController', function($scope,Auth) {
        
      $scope.submit = function() {
        Auth.register($scope.username,$scope.password).success(function(result) {
            $scope.result = result 
            console.log($scope.result);
        });
        

      };
    })

    .controller('AuthController',  function($scope,Auth) {
          $scope.submit = function() {
              Auth.login($scope.username,$scope.password, function(result){
                  $scope.result = result   
                  console.log($scope.result);            
              });
          }
          
 
    })

    .controller('PageController',  function($scope,PageResource) {
          $scope.pages = PageResource.query();     
    })

  .controller('RegisterCtrl', function ($scope, djangoAuth, Validate) {
  	$scope.model = {'username':'','password':'','email':''};
  	$scope.complete = false;
    $scope.register = function(formData){
      $scope.errors = [];
      Validate.form_validation(formData,$scope.errors);
      if(!formData.$invalid){
        djangoAuth.register($scope.model.username,$scope.model.password1,$scope.model.password2,$scope.model.email)
        .then(function(data){
        	// success case
            console.log(data);
            if(data.status==0){
              $scope.complete = true;
            } else {
              $scope.errors.server = data;
              console.log($scope.errors.server);
            }
        	
        },function(data){
        	// error case
        	$scope.errors = data;
        });
      }
    }
  })


    .controller('TopicController',  function($scope,TopicResource) {
          $scope.topics = TopicResource.query();     
    })


    .controller('CommentCtrl', function($scope, $http, CommentResource,CommentListResource,$stateParams) {

            $scope.getlist = function() {
                CommentListResource.comments($stateParams.id,$stateParams.page).success(function(result) {
                    $scope.comments = result;
                  
                }); 
            }            
        
        $scope.submit = function() 
            {
            var in_data = { author: $scope.author, content: $scope.content, post: $stateParams.id };  
            r = CommentResource.save(in_data,function()
                    { 
                        console.log(r);
                        CommentListResource.comments($stateParams.id,1).success(function(result) 
                            {
                                $scope.comments = result;
                            });   
            
                    },function(){alert('Error!')});
                $scope.getlist();            
            };


            $scope.getlist();
                
    });








