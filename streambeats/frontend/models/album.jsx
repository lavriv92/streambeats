/** @jsx React.DOM */

var Backbone = require('backbone');

var Album = Backbone.Model.extend({
  url: '/api/tracks/albums/'
});

module.exports = Album;
