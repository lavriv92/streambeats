/** @jsx React.DOM */

var React = require('react');
var Artists = require('../../collections/artists.jsx');

module.exports = React.createClass({
  collection: new Artists(),
  getInitialState: function() {
    return {artists: []};
  },

  componentDidMount: function() {
    var self = this;
    this.collection.on('sync', function(data) {
      self.setState({artists: self.collection.toJSON()});
    });
    this.collection.fetch();
  },
  render: function() {
    var ArtistsNodes = this.state.artists.map(function(artist) {
      return (<div>
                <div>{artist.name}</div>
              </div>
        )
      });

    return (
        <div>
          <h2>Artists</h2>
          <div>{ArtistsNodes}</div>
        </div>
        )
  },
});
