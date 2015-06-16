var userservices = angular.module('user_manager.userservices',[]);

userservices.factory('User', function($http) {
  

  var User = function(data) {
    angular.extend(this, data);
  }


User.get=function($scope){

 $http.get('/user/user').success(function(data, status, headers, config) {
 	         $scope.user=data;
 	         console.log(data);

           
        
}).error(function(data, status, headers, config) {
// Handle the error
console.log("error")
  
});	

}



return User ;

});