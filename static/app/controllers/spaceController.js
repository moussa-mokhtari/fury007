

app.controller('spaceController', ['$scope','User',function($scope,User){

$scope.EditUsername=false;

User.get($scope);





// $scope.login= function(user){
	
// 	User.login(user);
// }


// $scope.showRegisterForm= function(){

// 	$scope.register_form= true ;
// }

// $scope.register=function(user){
	
// }




}]); 