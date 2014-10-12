/** @jsx React.DOM */

var Backbone = require('backbone');

var Album = Backbone.Model.extend({
  url: '/api/music/albums'
});

module.exports = Album;
