angular.module('AngularApp')
.directive('commentform', function () {
  return {
    restrict: 'E',
    scope: { post: '=post' },
    template: "<div>[[post]]</div>"
  };
});
