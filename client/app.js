// 'use strict';

// Declare app level module which depends on views and components
var app = angular.module('app', ['app.services']);

app.controller('ShopsController', function ($scope, ShopFactory) {
  $scope.shop = {};
  $scope.flag = false;
  $scope.errorFlag = false;
  $scope.error_text = '';
  $scope.loadFlag = false;

  $scope.resetFlags = function() {
    $scope.loadFlag = false;
    $scope.errorFlag = false;
    $scope.flag = false;
  };

  $scope.getShopData = function() {
    $scope.loadFlag = true;
    $scope.errorFlag = false;
    $scope.flag = false;
    if ($scope.name) {
      var name = $scope.name.split(' ').join('-').toLowerCase();
      if (name !== 'starbucks' || name !== 'peets' || name !== '') {
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
        } else if (name === 'philz') {
          name = 'philz-coffee';
        }
        $scope.name = '';
        $scope.flag = false;

        ShopFactory.getData(name)
          .then(function(resp) {
            $scope.loadFlag = false;
            if (typeof resp === "string") {
              $scope.errorFlag = true;
              $scope.error_text = resp;
            } else {
              $scope.shop = resp;
              $scope.shop.name = resp.name.split('-').join(' ');
              $scope.flag = true;
            }
          })
          .catch(function(err) {
            $scope.errorFlag = true;
            $scope.error_text = err;
            console.log('Error in getting shop data', err);
          });
      }
    } else {
      $scope.loadFlag = false;
      $scope.errorFlag = true;
      $scope.error_text = 'Please enter a valid coffee shop name';
      console.log('error', $scope.error_text);
    };
  };
});

