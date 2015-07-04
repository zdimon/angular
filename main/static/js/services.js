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
      register: register
    };

    return Auth;

    

    function login(username, password) {
      return $http.post('/api/login/', {
        username: username, password: password
      }).then(loginSuccessFn, loginErrorFn);

      function loginSuccessFn(data, status, headers, config) {
        if (data.data.token) {
            alert('Success!!');
        }

        $window.location = '/';
      }

      function loginErrorFn(data, status, headers, config) {
        console.error(data);
      }
    }

    function logout() {
      
      $window.location = '/';
    }

    function register(username, password, email) {
        $http.post('/api/register/', {
        username: username, password: password, email: email
      })
        .success(function(response) {
            return response;
        })
        .error(function(response) {
            return {'status': 'error'};
        });

      

    }

   
  }
})();
