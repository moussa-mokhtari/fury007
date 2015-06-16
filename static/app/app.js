
var app = angular.module('app',['ngRoute','user_manager.userservices']);
app.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('<%');
  $interpolateProvider.endSymbol('%>');
});


app.config(['$routeProvider', function($routeProvider) {
     $routeProvider.
         when('/', {
         templateUrl:'/space/show',
        controller: 'spaceController'        
       
      }). when('/settings/', {
         templateUrl:'/space/settings',
        controller: 'spaceController'        
       
      })
     ;

 }]) ;