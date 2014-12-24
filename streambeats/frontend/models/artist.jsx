/** @jsx React.DOM */


var Backbone = require('backbone');

var Artist = Backbone.Model.extend({
  url: '/api/music/artist'
});

module.exports = Artist;
