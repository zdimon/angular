(function () {
  'use strict';


/// Service with Post and Topic resources

  angular
    .module('AngularApp')
    .factory('PostResource', function(djResource){
        return djResource('/api/posts/:id', {'id': "@id"});
    });

  angular
    .module('AngularApp')
    .factory('TopicResource', function(djResource){
        return djResource('/api/topic/:id/', {'id': "@id"});
    });


  angular
    .module('AngularApp')
    .factory('PostsResource', function(){
            return {'posts': function(topic_id){
                return $http.post('/api/posts/'+topic_id, {});
            }}
        }
    });




})();
