/** @jsx React.DOM */

var React = require('react');
var page = require('page');

var Artists = require('../music/artists.jsx');
var Albums = require('../music/albums.jsx');

var routes = [
  {
    'path': '/',
    'page':<h1>Page1</h1>
  },
  {
    'path': '/music/artists',
    'page': <Artists/>
  },
  {
    'path': '/music/albums',
    'page': <Albums/>
  },
  {
    'path': '/music/artists/:id',
    'page': <h1>Artist</h1>
  }
]

module.exports = React.createClass({

  getInitialState: function() {
    return {page: routes[0]['page']}
  },
  
  componentDidMount: function() {
    var self = this;

    routes.map(function(route) {
      page(route['path'], function(ctx) {
        return self.setState({page: route['page']});
      });
    });


    page.start();
  },

  render: function() {
    return this.state.page;
  }
});
