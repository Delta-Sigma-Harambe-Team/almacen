/**
* IndexController
* @namespace thinkster.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('thinkster.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope','$pusher','Authentication', 'Posts', 'Snackbar'];

  /**
  * @namespace IndexController
  */
  function IndexController($scope, $pusher, Authentication, Posts, Snackbar) {
    var vm = this;
    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.posts = [];

    //Seteamos el pusher global
    window.client = new Pusher('5b507c0f890e03302c2c',{encrypted: true});

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf thinkster.layout.controllers.IndexController
    */
    function activate() 
    {
      var my_channel = $pusher(client).subscribe('channel_almacen');
      my_channel.bind('new_petition',function(data) 
        {
          Snackbar.show('Nueva peticion de '+data.message);
        }
      );

      if (vm.isAuthenticated||1)  //Si queremos ver los posts aun NO authenticated
      { 
        Posts.all().then(postsSuccessFn, postsErrorFn);
      }

      $scope.$on('post.created', function (event, post) {
        vm.posts.unshift(post);
      });

      $scope.$on('post.created.error', function () {
        vm.posts.shift();
      });


      /**
      * @name postsSuccessFn
      * @desc Update posts array on view
      */
      function postsSuccessFn(data, status, headers, config) 
      {
        vm.posts = data.data;
      }


      /**
      * @name postsErrorFn
      * @desc Show snackbar with error
      */
      function postsErrorFn(data, status, headers, config) 
      {
        Snackbar.error(data.error);
      }
    }
  }
})();