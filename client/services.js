angular.module('app.services', [])
.factory('ShopFactory', function ($http) {
  var getData = function(name) {
    return $http({
      method: 'GET',
      url: '/shops/' + name + '/data'
    })
    .then(function(resp) {
      if (resp.status === 200) {
        return resp.data;
      } else {
        return 'Sorry, we cannot find that coffee shop... Maybe it\'s too hipster...';
      }
    });
  };

  return {
    getData: getData
  };
});

