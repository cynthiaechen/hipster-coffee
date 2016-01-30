var path = require('path');
var mongodb = require('mongodb');
var express = require('express');
var app = express();
//middleware
var morgan = require('morgan');
var parser = require('body-parser');

//database connection
var MongoClient = require('mongodb').MongoClient;
var db;

//initialize db connection

MongoClient.connect('mongodb://localhost:27017/shops', function(err, database) {
  if (err) {
    console.error(err);
  } else {
    console.log('Database is connected!');
  }
  db = database;

  var port = process.env.PORT || 3000;

  app.use(express.static(path.resolve(__dirname, '..', 'client')));

  app.listen(port);
  console.log('Listening to port 3000...');
});


app.get('/shops/:name/data', function(req, res, next) {
  db.collection('coffee_shops').findOne({name: req.params.name}, function(err, data) {
    if (err) {
      console.error(err);
      res.sendStatus(500);
    }
    if (data) {
      res.json(data);
    }
  });
});

module.exports = app;
