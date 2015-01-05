/** @jsx React.DOM */

var Backbone = require('backbone');
var Album = require('../models/album.jsx');


var Albums = Backbone.Collection.extend({
  url: '/api/tracks/albums/'
});

module.exports = Albums;
