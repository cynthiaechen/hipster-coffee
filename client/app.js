// 'use strict';

// Declare app level module which depends on views and components
var app = angular.module('app', ['app.services']);

app.controller('ShopsController', function ($scope, ShopFactory) {
  $scope.shop = {};
  $scope.flag = false;
  $scope.errorFlag = false;

  $scope.getShopData = function() {
    var name = $scope.name.split(' ').join('-').toLowerCase();
    if (name !== 'starbucks' || name !== 'peets') {
      if (name === 'blue-bottle') {
        name = 'blue-bottle-coffee-co';
      } else if (name === 'ritual') {
        name = 'ritual-coffee-roasters';
      } else if (name === 'sightglass') {
        name = 'sightglass-coffee';
      } else if (name === 'contraband') {
        name = 'contraband-coffee-bar';
      } else if (name === 'reveille') {
        name = 'reveille-coffee-co.'
      } else if (name === 'four-barrel') {
        name = 'four-barrel-coffee';
      } else if (name === 'trouble-coffee') {
        name = 'trouble-coffee-company';
      } else if (name === 'the-station') {
        name = 'the-station-sf';
      } else if (name === 'flywheel') {
        name = 'flywheel-coffee-roasters';
      }
      $scope.name = '';
      $scope.flag = false;
      ShopFactory.getData(name)
        .then(function(resp) {
          $scope.shop = resp;
          $scope.shop.name = resp.name.split('-').join(' ');
          $scope.flag = true;
          console.log('shop data', $scope.shop);
        })
        .catch(function(err) {
          $scope.errorFlag = true;
          $scope.error = 'Sorry, we cannot find that coffee shop... Maybe it\'s too hipster...';
          console.log('Error in getting shop data', err);
        });
    }
  };
});

