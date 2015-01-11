/** @jsx React.DOM */

var React = require('react');

var Menu = React.createClass({
  render: function() {
    return (
      <div className="col-md-12 centered bg-green bordered-bottom">
        <div className="menu">
          <a href="/music/artists/">Artists</a>
          <a href="/music/albums/">Albums</a>
          <a href="/music/genres/">Genres</a>
        </div>
      </div>
    )
  }
});

module.exports = Menu;
