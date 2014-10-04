/** @jsx React.DOM */

var React = require('react');
var page = require('page');

var routes = [
  {
    'path': '/',
    'page':<h1>Page1</h1>
  },
  {
    'path': '/test',
    'page': <h1>Page2</h1>
  }
]

module.exports = React.createClass({

  getInitialState: function() {
    return {page: routes[0]['page']}
  },
  
  componentDidMount: function() {
    var self = this;

    routes.map(function(route) {
      page(route['path'], function() {
        return self.setState({page: route['page']});
      });
    });


    page.start();
  },

  render: function() {
    return this.state.page;
  }
});
