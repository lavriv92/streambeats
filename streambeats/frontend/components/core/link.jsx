/** @jsx React.DOM */

var React = require('react');
var page = require('page');

module.exports = React.createClass({
  navigate: function(path) {
    return function() {
      page(path);
    }
  },

  render: function() {
    return <a onClick={this.navigate(this.props.path)}>{this.props.text}</a>
  }
});
