angular.module('app.controllers', [])
    
    .controller('RegistrationController', function($scope,Auth) {
        
      $scope.submit = function() {
        r = Auth.register($scope.username,$scope.password)
        console.log(r);
        
        //if (parseInt(result.status)==0) {
        //    alert('0');
       // } else {
        //    alert('1');     
       // }
      };
    })

    .controller('AuthController',  function($scope,Auth) {
      $scope.submit = function() {
          Auth.login($scope.username,$scope.password);
      };
    })

