/** @jsx React.DOM */

var Backbone = require('backbone');
var Artist = require('../models/artist.jsx');

var Artists = Backbone.Collection.extend({
  model: Artist
});

module.exports = Artists;
