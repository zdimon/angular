angular.module('app.controllers', [])
    
    .controller('RegistrationController', function($scope,Auth) {
        
      $scope.submit = function() {
        Auth.register($scope.model.username,$scope.model.password).success(function(result) {
            $scope.result = result 
            console.log($scope.result);
        });
        

      };
    })

    .controller('AuthController',  function($scope,Auth) {
          $scope.submit = function() {
              alert($scope.username);
              Auth.login($scope.username,$scope.password).then(function(result){
                    
                  $scope.rez = result.data;
                  if($scope.rez.status==1) {
                        $scope.isError = true; 
                    } else {
                        $scope.isSuccess = true; 
                    }
                  //$scope.$apply();
                  console.log($scope.res);
                   

                });
             $scope.result = { 'status':1,  'message': "User does not found!"};
               
          }
        //$scope.result = { 'status': 1,  'message': "User does not found!"}
        $scope.toggleModal = function() {
            $scope.modalShown = !$scope.modalShown;
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


    .controller('CommentCtrl', function($scope, $http, CommentResource,CommentListResource,$stateParams, $window) {
                
                CommentListResource.comments($stateParams.id,$stateParams.page).success(function(result) {
                    $scope.comments = result;
                });          
        
        $scope.submit = function() 
            {
             var in_data = { author: $scope.author, content: $scope.content, post: $stateParams.id };  
             r = CommentResource.save(in_data,function()
                    { 
                        CommentListResource.comments($stateParams.id,2).success(function(result) 
                            {
                                $scope.setComments(result);
                                $window.location.reload();
                                
                            });          
                    },function(){alert('Error!')});
            };

                
    })

   







