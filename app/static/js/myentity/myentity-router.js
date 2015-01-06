'use strict';

angular.module('myapp')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/myentities', {
        templateUrl: 'views/myentity/myentities.html',
        controller: 'MyentityController',
        resolve:{
          resolvedMyentity: ['Myentity', function (Myentity) {
            return Myentity.query();
          }]
        }
      })
    }]);
