/** @jsx React.DOM */

var React = require('react');

var Left = React.createClass({
  render: function() {
    return (
      <div className="container-fluid left" id="left">
        <div className="row">
          <div><a href="/music/albums">Albums</a></div>
          <div><a href="/music/artists">Artists</a></div>
        </div>
      </div>
      )
  }
});

module.exports = Left;
