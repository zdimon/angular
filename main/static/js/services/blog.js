(function () {
  'use strict';


/// Service with Post and Topic resources

  angular
    .module('AngularApp')
    .factory('PostResource', function(djResource){
        return djResource('/api/post/:id', {'id': "@id"});
    });

  angular
    .module('AngularApp')
    .factory('TopicResource', function(djResource){
        return djResource('/api/topic/:id/', {'id': "@id"});
    });


  angular
    .module('AngularApp')
    .factory('PostsResource',  function($http) {
            return {'posts': function(topic_id,page){
                return $http.get('/api/posts/'+topic_id+'?page='+page, {});
            }}
        
    });

  angular
    .module('AngularApp')
    .factory('CommentListResource',  function($http) {
            return {'comments': function(post_id,page){
                return $http.get('/api/comment/'+post_id+'?page='+page, {});
            }}
        
    });



})();
