/** @jsx React.DOM */

var React = require('react');

module.exports = React.createClass({
  render: function() {
    return (
      <div className="container-fluid" id="header">
        <div className="row">
          <h1 className="navbar-brand">StreamBeats</h1>
        </div>
      </div>
      )
  }
});
