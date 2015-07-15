(function () {
  'use strict';

  angular
    .module('AngularApp')
    .factory('Auth', Auth);

  Auth.$inject = ['$http', '$window'];

  function Auth($http, $window) {

    var Auth = {
      login: login,
      logout: logout,
      register: register,
      isauth: isauth,
    };
    
    return Auth;
    
    

    function login(username, password) {
      return $http.post('/api/login/', {
        username: username, password: password
      });
 
    }


    function logout(callback) {
      return $http.post('/api/logout/').success(callback); 
    }

    function isauth(callback) {
      return $http.get('/api/isauth/').success(callback); 
    }



    function register(username, password, email) {
        return $http.post('/api/register/', {
        username: username, password: password, email: email
      });
    }

   
  }



/// Service with Page resource

  angular
    .module('AngularApp')
    .factory('PageResource', function(djResource){
        return djResource('/api/page/:id/', {'id': "@id"});
    });

// Comment resource
  angular
    .module('AngularApp')
    .factory('CommentResource', function(djResource){
        return djResource('/api/comment/:id/', {'id': "@id"});
    });









})();
