/** @jsx React.DOM */


var Backbone = require('backbone');

var Artist = Backbone.Model.extend({
  url: '/api/tracks/artists/'
});

module.exports = Artist;
