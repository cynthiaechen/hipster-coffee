// var env = require('./process.env');
var path = require('path');
var mongodb = require('mongodb');
var express = require('express');
var app = express();
//middleware
var morgan = require('morgan');
var parser = require('body-parser');

//database connection
var MongoClient = require('mongodb').MongoClient;
// var uri = process.env.MONGOLAB_URI;
var uri = ENV['PROD_MONGODB'];
var db;

//initialize db connection

MongoClient.connect(uri, function(err, database) {
  if (err) {
    console.error(err);
  } else {
    console.log('Database is connected!');
  }
  db = database;

  var port = process.env.PORT || 3000;

  app.use(express.static(path.resolve(__dirname, '..', 'client')));

  app.listen(port);
  console.log('Listening to port ' + port + '...');
});


app.get('/shops/:name/data', function(req, res, next) {
  db.collection('coffee_shops').findOne({name: req.params.name}, function(err, data) {
    if (err) {
      console.error(err);
      res.sendStatus(500);
    }
    if (data) {
      res.json(data);
    } else {
      res.sendStatus(204);
    }
  });
});

module.exports = app;
