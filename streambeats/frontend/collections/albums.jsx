/** @jsx React.DOM */

var Backbone = require('backbone');
var Album = require('../models/album.jsx');


module.exports = Backbone.Collection.extend({
  model: Album
});
