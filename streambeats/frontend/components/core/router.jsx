/** @jsx React.DOM */

var React = require('react');
var page = require('page');

module.exports = React.createClass({

  getInitialState: function() {
    return {page: <h1>Page1</h1>}
  },
  
  conponentDidMount: function() {
    var self = this;

    page('/', function() {
      self.setState({page: <h1>Page1</h1>})
    });

    page('/test', function() {
      console.log('hello');
      self.setState({page: <h1>Page2</h1>});
    });

    page.start();
  },

  render: function() {
    return this.state.page;
  }
});
