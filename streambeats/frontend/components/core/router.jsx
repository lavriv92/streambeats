/** @jsx React.DOM */

var React = require('react');
var Backbone = require('backbone');

var Artists = require('../music/artists.jsx');
var Albums = require('../music/albums.jsx');
var Genres = require('../music/genres.jsx');


module.exports = React.createClass({

  getInitialState: function() {
    return {page: <h1>Home</h1>}
  },

  componentWillMount: function() {
    var Router = Backbone.Router.extend({
      routes: {
        '': this.routeHome,
        'music/artists/': this.routeArtists,
        'music/albums/': this.routeAlbums
      }
    });

    new Router();
    Backbone.history.start({pushState: true});
  },

  routeHome: function() {
    this.setState({
      page: <h1>Hello</h1>
    });
  },

  routeArtists: function() {
    this.setState({
      page: <Artists/>
    });
  },

  routeAlbums: function() {
    this.setState({
      page: <Albums/>
    });
  },

  render: function() {
    return this.state.page;
  }
});
