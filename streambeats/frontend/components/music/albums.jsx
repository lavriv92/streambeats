/** @jsx React.DOM */

var React = require('react');
var Albums = require('../../collections/albums.jsx');

module.exports = React.createClass({
  getInitialState: function() {
    var albums = new Albums();
    albums.fetch();
    console.log(albums);
    return {};
  },  
  
  componentDidMount: function() {},  
  
  render: function() {
    return (
        <div>
          <h2 className="page-header">Albums</h2>
          <div></div>
        </div>
        )
  }
});
