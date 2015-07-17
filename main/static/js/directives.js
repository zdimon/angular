(function () {
  'use strict';

  angular
    .module('AngularApp')
    .directive('userPanel', function() {
  return {
            templateUrl: 'static/templates/_user_panel.html',
            scope: false
         };
    });


})();
