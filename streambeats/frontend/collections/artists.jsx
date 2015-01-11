/** @jsx React.DOM */

var Backbone = require('backbone');
var Artist = require('../models/artist.jsx');

var Artists = Backbone.Collection.extend({
  url: '/api/tracks/artists/'
});


module.exports = Artists;
