angular.module('app.services', [])
.factory('ShopFactory', function ($http) {
  var getData = function(name) {
    return $http({
      method: 'GET',
      url: '/shops/' + name + '/data'
    })
    .then(function(resp) {
      return resp.data;
    });
  };

  return {
    getData: getData
  };
});

