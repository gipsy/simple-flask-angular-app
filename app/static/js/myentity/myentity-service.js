'use strict';

angular.module('myapp')
  .factory('Myentity', ['$resource', function ($resource) {
    return $resource('myapp/myentities/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
